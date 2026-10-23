// Decodificador del QR animado (el mismo codigo fuente que core/qr_transfer.py, bit a bit). Sin DOM: se prueba en Node.
const HEADER = 17;
const VERSION = 1;
const DEGREES = [0.10, 0.60, 0.77, 0.85, 0.90, 0.94, 0.97, 1.00];

function mulberry32(seed) {
  let a = seed | 0;
  return () => {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return (t ^ (t >>> 14)) >>> 0;
  };
}

export function indices(transferId, seq, k) {
  if (seq % 2 === 0) return [Math.floor(seq / 2) % k];
  const rng = mulberry32((transferId ^ Number((BigInt(seq) * 2654435761n) & 0xFFFFFFFFn)) >>> 0);
  const roll = rng() / 2 ** 32;
  const degree = Math.min(DEGREES.findIndex((edge) => roll < edge) + 1, k);
  const chosen = [];
  while (chosen.length < degree) {
    const value = rng() % k;
    if (!chosen.includes(value)) chosen.push(value);
  }
  return chosen.sort((x, y) => x - y);
}

function xorInto(target, source) {
  for (let i = 0; i < target.length; i++) target[i] ^= source[i];
}

export class Decoder {
  constructor() { this.reset(null); }

  reset(id) {
    this.transferId = id;
    this.total = this.blockSize = this.k = 0;
    this.known = new Map();
    this.pending = [];
    this.seen = new Set();
  }

  get done() { return this.k > 0 && this.known.size === this.k; }
  get progress() { return this.k ? this.known.size / this.k : 0; }

  /** Anade un fotograma (bytes del QR). Devuelve true si era de Kreix. */
  add(frame) {
    if (frame.length < HEADER || frame[0] !== 0x4B || frame[1] !== 0x58 || frame[2] !== VERSION) return false;
    const view = new DataView(frame.buffer, frame.byteOffset, frame.byteLength);
    const id = view.getUint32(3), total = view.getUint32(7), blockSize = view.getUint16(11), seq = view.getUint32(13);
    if (frame.length !== HEADER + blockSize) return false;
    if (id !== this.transferId) {
      this.reset(id);
      this.total = total;
      this.blockSize = blockSize;
      this.k = Math.max(1, Math.ceil(total / blockSize));
    }
    if (this.seen.has(seq) || this.done) return true;
    this.seen.add(seq);
    this.absorb(new Set(indices(id, seq, this.k)), frame.slice(HEADER));
    return true;
  }

  absorb(chosen, payload) {
    const queue = [[chosen, payload]];
    while (queue.length) {
      const [set, data] = queue.pop();
      for (const i of [...set]) if (this.known.has(i)) { xorInto(data, this.known.get(i)); set.delete(i); }
      if (!set.size) continue;
      if (set.size > 1) { this.pending.push([set, data]); continue; }
      const [index] = set;
      this.known.set(index, data);
      const still = [];
      for (const item of this.pending) (item[0].has(index) ? queue : still).push(item);
      this.pending = still;
    }
  }

  result() {
    const out = new Uint8Array(this.k * this.blockSize);
    for (let i = 0; i < this.k; i++) out.set(this.known.get(i), i * this.blockSize);
    return out.slice(0, this.total);
  }
}

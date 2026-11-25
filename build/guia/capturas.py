"""Capturas en tema claro del programa de Windows para la guía en PDF (datos de demostración, nunca datos reales).

Uso:  KREIX_REPO=RUTA/kreix KREIX_LANG=ca RUTA/kreix/.venv/Scripts/python build/guia/capturas.py
      (KREIX_LANG: es por defecto, ca o en; KREIX_REPO: la carpeta del repo kreix, con su origin/main al dia)
Salida: build/guia/img/pc-*.png (castellano) o build/guia/img/<idioma>/pc-*.png
"""
from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime
from decimal import Decimal
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QT_QPA_FONTDIR", r"C:\Windows\Fonts")

KREIX = Path(os.environ.get("KREIX_REPO", r"C:\Users\dssua\kreix"))
LANG = os.environ.get("KREIX_LANG", "es")
OUT = Path(__file__).resolve().parent / "img" / ("" if LANG == "es" else LANG)
sys.path.insert(0, str(KREIX))
sys.path.insert(0, str(KREIX / "tools"))

from PySide6.QtCore import QDate  # noqa: E402
from PySide6.QtTest import QTest  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

import demo_data  # noqa: E402
from core.enums import TxCategory  # noqa: E402
from main import build_window  # noqa: E402
import screenshots as base  # noqa: E402


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    as_of = demo_data.build(tmp / "demo")
    app = QApplication(sys.argv[:1])
    app.setStyle("Fusion")
    from ui import fonts
    fonts.setup_application(app)
    db = f"sqlite:///{tmp / 'demo.db'}"
    if LANG != "es":                                   # el idioma se guarda antes: la ventana nace ya en ese idioma
        from dataclasses import replace
        first = build_window(db, "demo")
        first._svc.settings.save(replace(first._settings, language=LANG))
        first.deleteLater()
    window = build_window(db, "demo")
    window.clock = window.dashboard.clock = lambda: datetime.now().replace(hour=11, minute=30, second=0, microsecond=0)   # el saludo es de dia, sea la hora que sea
    window.show()
    window._apply_user_name("Blitzen", announce=False)
    window.apply_theme("light")

    def shot(name: str, widget=None) -> None:
        QTest.qWait(1800)
        (widget or window).grab().save(str(OUT / f"pc-{name}.png"))

    window.resize(1280, 1180)
    shot("bienvenida")
    window.navigate(window.IMPORT)
    window.import_view.as_of.setDate(QDate(as_of.year, as_of.month, as_of.day))
    window.import_view.preview_paths([str(p) for p in sorted((tmp / "demo").glob("*.csv"))])
    shot("importar")
    window.import_view.confirm_import()
    window._svc.categories.save_budgets({TxCategory.GROCERIES: Decimal(250), TxCategory.LEISURE: Decimal(30),
                                         TxCategory.DINING: Decimal(60), TxCategory.TRANSPORT: Decimal(40)})
    window.refresh()
    for name, page in (("inicio", window.SUMMARY), ("cuentas", window.ACCOUNTS), ("inversion", window.INVESTMENT),
                       ("exportar", window.EXPORT), ("ajustes", window.SETTINGS), ("ayuda", window.HELP)):
        window.resize(1280, 1900 if page in (window.ACCOUNTS, window.SETTINGS) else 1180)
        window.navigate(page)
        shot(name)

    from ui.lock_screen import LockDialog, LockMode
    from ui.mapping_dialog import MappingDialog
    csv = tmp / "otro-banco.csv"
    csv.write_text(base.BANK_CSV, encoding="utf-8")
    dialog = MappingDialog(window._svc.importer, str(csv), window)
    dialog.show()
    shot("otro-banco", dialog)
    dialog.close()
    lock = LockDialog(LockMode.CREATE, lambda _password: None)
    lock.password.setText("correcto caballo bateria grapa")
    lock.confirm.setText("correcto caballo bateria grapa")
    lock.show()
    shot("bloqueo", lock)
    lock.close()
    app.quit()
    print("Capturas en", OUT)


if __name__ == "__main__":
    main()

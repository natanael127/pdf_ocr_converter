# -*- mode: python ; coding: utf-8 -*-


a = Analysis(['pdf_ocr_converter.py'],
             pathex=[],
             binaries=[],
             datas=[('C:/Users/natan/AppData/Local/Programs/Python/Python311/Lib/site-packages/ocrmypdf/data/*', 'ocrmypdf/data')],
             hiddenimports=['ocrmypdf'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pdf_ocr_converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

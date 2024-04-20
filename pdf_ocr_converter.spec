from PyInstaller.utils.hooks import collect_data_files

# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pdf_ocr_converter.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('env/Lib/site-packages/ocrmypdf-16.2.0.dist-info/*', 'ocrmypdf-16.2.0.dist-info'),
        *collect_data_files('ocrmypdf', include_py_files=True)
    ],
    hiddenimports=['ocrmypdf','PIL'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
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
    icon='ocr.ico'
)

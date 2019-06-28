# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\comap_hr_scan\\rename_pdfs.py'],
             pathex=['c:\\projects\\other\\comap-hr-scan'],
             binaries=[],
             datas=[('installer_data\\*', '.'),
                    ('installer_data\\tessdata\\*', '.\\tessdata')],
             hiddenimports=['distutils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='rename_pdfs',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bin')

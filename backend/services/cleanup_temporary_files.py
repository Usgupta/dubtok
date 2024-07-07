import os
import glob

def cleanup_temporary_files():
    folders = ["output/*", "../ai/output_audio/*", "../ai/chunks/*", "../uploads/*"]
    
    for folder in folders:        
        files = glob.glob(folder)
        for f in files:
            if os.path.basename(f) != '.gitignore':
                try: 
                    os.remove(f)
                except Exception as e:
                    print(f'Cannot remove {f}: {e}')
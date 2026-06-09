# Redirection wrapper for backward compatibility with notebooks and tests.
import sys
from pathlib import Path

# 1. Identify paths
local_utils_dir = Path(__file__).resolve().parent
local_stage_dir = local_utils_dir.parent
src_dir = local_stage_dir.parent

# 2. Adjust sys.path to prioritize central src/ over local stage directory
sys_path_backup = sys.path.copy()
sys.path = [p for p in sys.path if Path(p).resolve() != local_stage_dir.resolve()]
src_dir_str = str(src_dir)
if src_dir_str not in sys.path:
    sys.path.insert(0, src_dir_str)

# 3. Backup and temporarily remove "utils" from sys.modules to prevent recursion
sys_modules_backup = {}
for k in list(sys.modules.keys()):
    if k == "utils" or k.startswith("utils."):
        sys_modules_backup[k] = sys.modules.pop(k)

try:
    # Perform absolute import of the central module
    module_name = Path(__file__).stem
    central_module_name = f"utils.winsorizacao"
    central_module = __import__(central_module_name, fromlist=["*"])
finally:
    # Restore sys.path and sys.modules
    sys.path = sys_path_backup
    for k, v in sys_modules_backup.items():
        sys.modules[k] = v

# 4. Export all symbols to local namespace
globals().update({k: v for k, v in central_module.__dict__.items() if not k.startswith("__")})

#!/usr/bin/env python3
import json
import os
import shutil
import sys
import psutil

def get_system_health():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu_usage_pct": cpu_percent,
        "memory_used_pct": memory.percent,
        "memory_available_mb": round(memory.available / (1024 * 1024), 2),
        "disk_used_pct": disk.percent,
        "disk_free_gb": round(disk.free / (1024 * 1024 * 1024), 2),
        "status": "HEALTHY" if cpu_percent < 85 and memory.percent < 90 else "DEGRADED"
    }

if __name__ == '__main__':
    print(json.dumps(get_system_health(), indent=2))

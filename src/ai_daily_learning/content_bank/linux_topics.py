"""Linux Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class LinuxTopicProvider(BaseTopicProvider):
    """Generates rich Linux tips & command guides for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Linux")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Advanced Process & Memory Profiling using `htop`, `vmstat`, and `lsof`",
                "Intermediate",
                "Diagnosing system memory pressure, thread lockups, and open file descriptors is critical for production Linux server management.",
                """# 1. View memory usage and virtual memory stats every 2 seconds
vmstat -S M 2 5

# 2. List all active listening TCP ports and holding processes
sudo lsof -iTCP -sTCP:LISTEN -n -P

# 3. Find top 5 memory-consuming processes formatted by PID and command name
ps aux --sort=-%mem | head -n 6 | awk '{print $2, $4, $11}'""",
                [
                    "`vmstat` tracks swap-in/swap-out (si/so) to detect RAM exhaustion.",
                    "`lsof -i -n -P` bypasses slow DNS reverse lookups for rapid port auditing.",
                    "`ps aux --sort` allows custom scriptable process sorting."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            tips = [
                "Mastering AWK Text Processing & Column Aggregations",
                "Writing Systemd Service Units with Auto-Restart & Resource Limits",
                "SSH Tunneling, Port Forwarding, and Dynamic SOCKS Proxies",
                "File Access Control Lists (FACL) with setfacl and getfacl",
                "Network Packet Sniffing with tcpdump and TShark Filters",
                "Linux Kernel Parameter Tuning via sysctl.conf",
                "Cgroups v2 and Resource Quota Allocation for Processes",
                "Managing Disk Storage with LVM (Logical Volume Manager)",
                "Automating Backup Pipelines with rsync, tar, and gpg",
                "Analyzing System Logs with journalctl and logrotate"
            ]
            selected = tips[(day_idx - 1) % len(tips)]
            title = f"{selected} (Day {day_idx})"
            diff = "Intermediate"
            concept = f"Linux administration guide for {selected}. Essential commands and automation patterns for cloud infrastructure."
            code = f"""# Linux Command Guide Day {day_idx}: {selected}

# Check system status
uname -a
uptime

# Execute demonstration script
echo "Running system check for: {selected}"
df -h / | awk 'NR==2 {{print "Disk Usage: " $5}}'"""
            takeaways = [
                f"Master {selected} for DevOps and SysAdmin mastery.",
                "Always check command exit statuses (`$?`) in automated bash scripts.",
                "Use systemd limits (`MemoryMax`, `CPUQuota`) to prevent runaway process crashes."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )

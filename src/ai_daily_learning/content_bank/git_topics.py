"""Git Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class GitTopicProvider(BaseTopicProvider):
    """Generates rich Git tips & workflow guides for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Git")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Git Worktrees & Recovering Lost Commits via `git reflog`",
                "Advanced",
                "Git Worktrees enable checking out multiple branches simultaneously in separate directories without stashing or switching contexts in your main directory.",
                """# 1. Add a separate worktree for parallel feature development
git worktree add ../feature-auth-fix feature/auth-fix

# 2. List all active worktrees
git worktree list

# 3. Emergency: Recover a accidentally deleted commit or hard reset branch
git reflog
# Output: 7a8b9c0 HEAD@{1}: reset: moving to HEAD~3

# Restore branch head to lost commit
git checkout -b recovered-branch 7a8b9c0""",
                [
                    "Worktrees isolate working trees sharing a single `.git` repository object database.",
                    "`git reflog` tracks every HEAD movement, enabling recovery of deleted commits for up to 90 days.",
                    "Clean up finished worktrees using `git worktree remove <path>`."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            tips = [
                "Interactive Rebase (`git rebase -i`) Masterclass",
                "Binary Search Bug Hunting with `git bisect run`",
                "Custom Client-Side Hooks & Pre-commit Enforcement",
                "Git Submodules vs Git Subtree for Monorepos",
                "Cherry-Picking Commits across Divergent Branches",
                "Configuring Advanced Aliases and Custom Git Subcommands",
                "Signing Commits with GPG / SSH Keys for Provenance",
                "Managing Large Binaries using Git LFS (Large File Storage)",
                "Resolving Complex Merge Conflicts with 3-Way Merge (`diff3`)",
                "Pruning Stale Remote Tracking Branches with `git fetch --prune`"
            ]
            selected = tips[(day_idx - 1) % len(tips)]
            title = f"{selected} (Day {day_idx})"
            diff = "Intermediate"
            concept = f"Mastering {selected} to maintain clean git history, streamline team collaboration, and debug regressions efficiently."
            code = f"""# Git Workflow Command Day {day_idx}: {selected}

# Check repository log with graph format
git log --graph --oneline --decorate --all -n 10

# Alias recommendation:
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit" """
            takeaways = [
                f"Master {selected} for professional software craftsmanship.",
                "Keep commit history atomic, readable, and cleanly bisect-able.",
                "Never force push (`git push --force`) to shared main branches without lease check (`--force-with-lease`)."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )

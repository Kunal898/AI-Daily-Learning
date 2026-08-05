"""Cybersecurity Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class CybersecurityTopicProvider(BaseTopicProvider):
    """Generates rich Cybersecurity educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Cybersecurity")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Modern JWT Vulnerabilities & Alg None / Key Confusion Mitigation",
                "Advanced",
                "JSON Web Tokens (JWT) must enforce strict signature algorithm verification. Insecure parsers can be tricked via `alg: none` or RSA/HMAC public key confusion attacks.",
                """# Python JWT Verification Hardening Example
import jwt
from typing import Dict, Any

SECRET_KEY = "super-secret-hmac-key"

def verify_and_decode_token(token_str: str) -> Dict[str, Any]:
    try:
        # Explicitly enforce signature algorithm and reject 'none' or mismatched types
        payload = jwt.decode(
            token_str,
            SECRET_KEY,
            algorithms=["HS256"],  # Whitelist approved algorithms ONLY
            options={
                "verify_signature": True,
                "verify_exp": True,
                "require": ["exp", "iss", "sub"]
            }
        )
        return payload
    except jwt.PyJWTError as e:
        raise ValueError(f"Security Alert: Invalid Token Attempt - {str(e)}")""",
                [
                    "Never trust client-specified `alg` headers blindly inside JWT decoders.",
                    "Always enforce signature checking and whitelist allowed signature algorithms explicitly.",
                    "Include strict expiration (`exp`) and audience/issuer assertions in all claim sets."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            topics = [
                "Zero Trust Architecture & Micro-segmentation Principles",
                "AES-256-GCM Authenticated Encryption vs Cipher Block Chaining (CBC)",
                "OWASP Top 10: Server-Side Request Forgery (SSRF) Hardening",
                "Content Security Policy (CSP) Level 3 Implementation & Nonce Usage",
                "Privilege Escalation Vectors in Linux SUID Binaries",
                "OAuth 2.1 PKCE Flow for Single Page Applications (SPAs)",
                "Static Application Security Testing (SAST) Integration in CI/CD",
                "DNS Over HTTPS (DoH) & TLS Fingerprinting (JA3/JA4)",
                "SQL Injection Mitigation using Parameterized Statements",
                "Container Hardening & Rootless Docker Security"
            ]
            selected = topics[(day_idx - 1) % len(topics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Advanced" if day_idx % 2 == 0 else "Intermediate"
            concept = f"Security concept breakdown for {selected}. Understanding attacker TTPs and implementing robust defense-in-depth security controls."
            code = f"""# Cybersecurity Hardening Script Day {day_idx}: {selected}
import secrets
import hashlib

def generate_secure_token() -> str:
    # 256-bit cryptographically secure entropy source
    random_bytes = secrets.token_bytes(32)
    return hashlib.sha256(random_bytes).hexdigest()

print(f"Generated Audit Nonce: {{generate_secure_token()}}")"""
            takeaways = [
                f"Apply key security controls for {selected}.",
                "Enforce principle of least privilege across all service boundaries.",
                "Automate continuous vulnerability scanning throughout dev pipelines."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )

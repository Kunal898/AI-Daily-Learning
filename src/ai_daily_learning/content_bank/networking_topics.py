"""Networking Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class NetworkingTopicProvider(BaseTopicProvider):
    """Generates rich Networking educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Networking")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "TLS 1.3 Handshake Architecture & 0-RTT Connection Resumption",
                "Advanced",
                "TLS 1.3 eliminates round trips during connection setup, reducing the cryptographic handshake from 2-RTTs down to 1-RTT (or 0-RTT for resumed sessions).",
                """# Python Low-Level TLS Socket Connection Example
import socket
import ssl

def inspect_tls_handshake(hostname: str = "example.com", port: int = 443) -> None:
    context = ssl.create_default_context()
    # Force modern TLS versions
    context.minimum_version = ssl.TLSVersion.TLS1_3
    
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as tls_sock:
            print(f"Connected to: {hostname}")
            print(f"SSL Protocol Version: {tls_sock.version()}")
            print(f"Cipher Suite Used: {tls_sock.cipher()}")
            cert = tls_sock.getpeercert()
            print(f"Certificate Issuer: {cert.get('issuer')}")

if __name__ == "__main__":
    inspect_tls_handshake()""",
                [
                    "TLS 1.3 encrypts handshakes earlier, concealing client certificates from eavesdroppers.",
                    "Disallows weak legacy ciphers (RC4, 3DES, static RSA key exchange) in favor of Ephemeral Diffie-Hellman (ECDHE).",
                    "0-RTT mode allows early data sending on session resumption but requires anti-replay protection."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            topics = [
                "TCP 3-Way Handshake & SYN Flood Attack Mitigation",
                "DNS Resolution Flow: Recursive Resolver vs Authoritative Nameservers",
                "HTTP/2 Multiplexing vs HTTP/3 QUIC (UDP Transport)",
                "CIDR Subnetting & IP Route Calculation in Python",
                "BGP Anycast Routing & Autonomous Systems (AS)",
                "WebSocket Protocol Handshake & Frame Decoding",
                "gRPC vs REST API Performance over HTTP/2",
                "Network Address Translation (NAT) & STUN/TURN Protocols",
                "eBPF (Extended Berkeley Packet Filter) Kernel Packet Inspection",
                "IPsec VPN Tunneling & Encapsulating Security Payload (ESP)"
            ]
            selected = topics[(day_idx - 1) % len(topics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Advanced" if day_idx % 2 == 0 else "Intermediate"
            concept = f"Core networking principles for {selected}. Analyzing packet flow, protocol mechanics, and low-latency system design."
            code = f"""# Networking Protocol Inspector Day {day_idx}: {selected}
import socket

def check_port(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2.0)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

print(f"Port 80 status: {{check_port('1.1.1.1', 80)}}")"""
            takeaways = [
                f"Understand packet mechanics for {selected}.",
                "Monitor network latency and TCP socket buffer bottlenecks.",
                "Enforce strict TLS encryption across all public network endpoints."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )

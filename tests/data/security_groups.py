DATA = [
    {
        "security_group": {
            "rules": [
                {
                    "to_port": 22,
                    "cidr": "0.0.0.0/0",
                    "from_port": 22,
                    "ip_protocol": "tcp"
                }
            ],
            "name": "ssh",
            "description": "Simply ssh port group"
        }
    },
]

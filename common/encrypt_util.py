# -*- coding: utf-8 -*-
import hashlib
import hmac


def md5_hex(text: str, encoding: str = "utf-8") -> str:
    return hashlib.md5(text.encode(encoding)).hexdigest()


def hmac_sha256_hex(secret: str, message: str, encoding: str = "utf-8") -> str:
    return hmac.new(secret.encode(encoding), message.encode(encoding), hashlib.sha256).hexdigest()

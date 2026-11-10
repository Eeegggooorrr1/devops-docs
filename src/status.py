"""Р¤РѕСЂРјРёСЂРѕРІР°РЅРёРµ СЃС‚СЂРѕРєРё СЃРѕСЃС‚РѕСЏРЅРёСЏ."""


def format_status(version: str, deployed: bool) -> str:
    """Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃРѕСЃС‚РѕСЏРЅРёРµ РїСѓР±Р»РёРєР°С†РёРё."""
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"


if __name__ == "__main__":
    print(format_status("1.0", deployed=True))

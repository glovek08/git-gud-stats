def get_language_resume(payload: dict) -> list[dict]:
    language_totals = {}

    for repo in payload["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            lang_name = edge["node"]["name"]
            lang_size = edge["size"]
            language_totals[lang_name] = language_totals.get(lang_name, 0) + lang_size

    # Convertir a lista de dicts y ordenar por size descendente
    language_list = [{"language": k, "size": v} for k, v in language_totals.items()]
    language_list.sort(key=lambda x: x["size"], reverse=True)

    return language_list
"""Prueba manual de conexión con la API de Claude.

Uso: python -m scripts.test_claude_api
Requiere ANTHROPIC_API_KEY configurada en backend/.env
"""

from anthropic import Anthropic

from app.config import settings


def main() -> None:
    if not settings.anthropic_api_key:
        raise SystemExit("ANTHROPIC_API_KEY no está configurada en backend/.env")

    client = Anthropic(api_key=settings.anthropic_api_key)
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=50,
        messages=[{"role": "user", "content": "Responde solo con: conexión exitosa"}],
    )
    print(response.content[0].text)


if __name__ == "__main__":
    main()

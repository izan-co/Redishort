# 🐦 Roadmap Educativo: Redishort v2 - Twitter/X Pivot

## 🎯 Visión del Proyecto

**Redishort v2** es un sistema autónomo de creación de YouTube Shorts que transforma **tweets virales de Twitter/X** en videos cortos de alto engagement, enfocado principalmente en **audiencia hispanohablante**.

### Diferenciadores Clave

| Aspecto | Decisión Estratégica | Por Qué |
|---------|---------------------|---------|
| **Fuente** | Tweets virales de X | Contenido fresco (minutos/horas vs días), altísimo engagement previo |
| **Idioma** | Español prioritario | Menos competencia que inglés, audiencia latinoamericana infra-servida |
| **Formato** | Reacción rápida sensacionalista | Retención alta, fomenta comentarios, viralidad por controversia |
| **Nicho** | Multi-nicho con series | Flexibilidad para pivotar según performance |
| **Tech** | Arquitectura profesional | Aprendizaje profundo, portfolio de calidad |

---

## 🧭 Filosofía del Roadmap

Este roadmap no es solo una guía técnica, es un **viaje educativo estructurado** para dominar:

1. **Arquitectura de software profesional** (Clean Architecture, DDD, SOLID)
2. **Ingeniería de datos** (ETL de APIs externas, detección de viralidad)
3. **Resiliencia y manejo de rate limits** (crítico con X API)
4. **Generación de contenido multimedia** (TTS, video composition)
5. **DevOps y observabilidad** (CI/CD, metrics, alerting)

### Principios Guía

- ✅ **Aprender haciendo**: Cada concepto se acompaña de implementación práctica
- ✅ **Ética primero**: Respeto a TOS de plataformas, atribución, moderación
- ✅ **Incremental**: Cada fase construye sobre la anterior
- ✅ **Production-ready**: Estándares profesionales desde día 1
- ✅ **Testeable**: Si no puedes probarlo, no funciona

---

## ⚠️ Consideraciones Críticas sobre X/Twitter API

### Realidad de X API (2025-2026)

| Tier | Precio | Limitaciones | Viabilidad |
|------|--------|--------------|------------|
| **Free** | $0 | 1,500 tweets/mes, solo lectura básica | ❌ Inviable para producción |
| **Basic** | $100/mes | 10,000 tweets/mes, 50 req/15min | ⚠️ Muy limitado |
| **Pro** | $5,000/mes | 1M tweets/mes | ✅ Viable pero caro |

**Aprende**: Tras la adquisición de Elon Musk, X API pasó de gratuita a extremadamente cara. Esto creó un problema para desarrolladores indie.

### Alternativas Pragmáticas

1. **API Oficial Basic** ($100/mes) + Rate Limiting agresivo
2. **Scraping Ético** (zona gris legal, alto riesgo de ban)
3. **Servicios de terceros** (Apify, ScraperAPI) - $50-200/mes
4. **Hybrid approach**: API oficial + fallback a scraping

**Recomendación para este roadmap**: Empezar con scraping ético para aprendizaje, migrar a API oficial cuando validemos el concepto.

---

## 📅 Duración Total Estimada: 9-10 semanas

| Fase | Duración | Enfoque Principal |
|------|----------|-------------------|
| Fase 0 | 1 semana | Setup, tooling, fundamentos |
| Fase 1 | 2 semanas | Core architecture (domain: tweets) |
| Fase 2 | 2 semanas | X/Twitter adapter + viralidad |
| Fase 3 | 2 semanas | Video pipeline (tweet visualization) |
| Fase 4 | 1 semana | YouTube upload & scheduler |
| Fase 5 | 1 semana | Testing & CI/CD |
| Fase 6 | 1 semana | Production & observability |

---

# 📚 Fase 0: Fundamentos y Setup (1 semana)

## Objetivos de Aprendizaje

- Entender el landscape de X API y sus restricciones
- Configurar entorno de desarrollo profesional
- Diseñar arquitectura inicial adaptada a tweets
- Establecer principios éticos de scraping

## Conceptos Clave a Estudiar

| Concepto | Por Qué Es Crítico | Aplicación en Proyecto |
|----------|-------------------|------------------------|
| **Rate Limiting** | X API tiene límites estrictos | Sistema de backoff y circuit breakers |
| **Web Scraping Ético** | Balance entre legal y práctico | robots.txt, delays, User-Agent honesto |
| **Detección de Viralidad** | No todos los tweets sirven | Algoritmo de scoring multifactorial |
| **Fair Use** | Evitar copyright strikes | Atribución, transformación de contenido |

## Implementación Práctica

### Paso 1: Estructura de Proyecto Profesional

```bash
redishort-v2-twitter/
├── src/
│   ├── redishort/
│   │   ├── __init__.py
│   │   ├── core/              # Lógica de negocio
│   │   │   ├── services.py
│   │   │   ├── viralitys_detector.py  # NUEVO: Detecta tweets virales
│   │   │   └── content_moderator.py   # NUEVO: Modera contenido
│   │   ├── domain/            # Modelos de dominio
│   │   │   ├── models.py      # Tweet, VideoScript, etc.
│   │   │   └── repositories.py
│   │   ├── adapters/          # Integraciones externas
│   │   │   ├── twitter_scraper.py     # NUEVO: Scraping ético
│   │   │   ├── twitter_api_adapter.py # NUEVO: API oficial
│   │   │   ├── gemini_adapter.py
│   │   │   ├── tts_adapter.py
│   │   │   └── youtube_adapter.py
│   │   ├── video/             # Pipeline de video
│   │   │   ├── tweet_visualizer.py    # NUEVO: Render tweet en imagen
│   │   │   └── video_composer.py
│   │   ├── config/
│   │   │   └── settings.py
│   │   └── observability/
│   │       ├── metrics.py
│   │       └── logging.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── assets/
│   ├── fonts/                 # Fuentes para tweets
│   ├── backgrounds/
│   └── overlays/              # Emojis, reactions, etc.
├── scripts/
│   ├── analyze_virality.py    # NUEVO: Analiza patrones de viralidad
│   └── test_twitter_access.py # NUEVO: Valida acceso a X
├── docs/
│   ├── ETHICS.md              # NUEVO: Guía ética
│   └── API_COMPARISON.md      # NUEVO: Comparación de APIs
├── docker/
│   ├── Dockerfile.dev
│   └── Dockerfile.prod
├── .github/
│   └── workflows/
├── pyproject.toml
├── Makefile
└── README.md
```

**Aprende**: Estructura adaptada a la naturaleza del proyecto
- `viralitys_detector.py`: Lógica específica para identificar tweets con potencial
- `content_moderator.py`: Evita contenido problemático (NSFW, hate speech)
- `twitter_scraper.py` vs `twitter_api_adapter.py`: Dos estrategias, misma interface

### Paso 2: Configuración con Validación de Acceso a X

```python
# src/redishort/config/settings.py
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr, validator
from enum import Enum

class TwitterSourceMode(str, Enum):
    """
    Aprende: Enum para modos de acceso a Twitter
    - API_OFFICIAL: X API oficial ($100-5000/mes)
    - SCRAPING: Web scraping ético (gratis, riesgo medio)
    - THIRD_PARTY: Servicios como Apify ($50-200/mes)
    """
    API_OFFICIAL = "api_official"
    SCRAPING = "scraping"
    THIRD_PARTY = "third_party"

class Settings(BaseSettings):
    """
    Aprende: Configuración exhaustiva con validación
    - Diferentes modos de acceso a X
    - Validación de coherencia (ej: si mode=API, debe haber bearer_token)
    - Defaults sensatos para desarrollo
    """

    # === Twitter/X Configuration ===
    twitter_source_mode: TwitterSourceMode = Field(
        default=TwitterSourceMode.SCRAPING,
        description="Modo de acceso a Twitter: api_official, scraping, o third_party"
    )

    # API Oficial (si twitter_source_mode == API_OFFICIAL)
    twitter_bearer_token: SecretStr | None = Field(
        default=None,
        description="Bearer token de X API v2 ($100/mes mínimo)"
    )

    # Scraping (si twitter_source_mode == SCRAPING)
    twitter_scraping_user_agent: str = Field(
        default="RedishortBot/2.0 (Educational Project; +https://github.com/tu-user/redishort-v2)",
        description="User-Agent honesto para scraping"
    )
    twitter_scraping_delay_sec: float = Field(
        default=2.0,
        description="Delay entre requests (segundos) para scraping ético"
    )

    # Third-party (si twitter_source_mode == THIRD_PARTY)
    apify_api_key: SecretStr | None = Field(default=None)

    # === Viralidad Detection ===
    virality_min_likes: int = Field(
        default=500,
        description="Mínimo de likes para considerar un tweet"
    )
    virality_min_retweets: int = Field(default=100)
    virality_min_replies: int = Field(default=50)
    virality_time_window_hours: int = Field(
        default=24,
        description="Solo tweets de las últimas N horas"
    )
    virality_preferred_language: str = Field(
        default="es",
        description="Idioma preferido: 'es' para español"
    )

    # === Content Moderation ===
    moderation_enabled: bool = Field(default=True)
    moderation_block_nsfw: bool = Field(default=True)
    moderation_block_hate_speech: bool = Field(default=True)

    # === Google AI (Gemini) ===
    google_api_key: SecretStr = Field(...)

    # === TTS ===
    tts_provider: str = Field(default="google_cloud")  # google_cloud, elevenlabs
    tts_voice_spanish: str = Field(
        default="es-ES-Studio-C",
        description="Voz en español para narración"
    )
    tts_speaking_rate: float = Field(
        default=1.1,
        description="Velocidad de habla (>1.0 = más rápido, sensacionalista)"
    )

    # === YouTube ===
    youtube_client_secrets_file: str = Field(default="client_secrets.json")
    youtube_daily_quota: int = Field(default=10000)

    # === App Config ===
    log_level: str = Field(default="INFO")
    environment: str = Field(default="development")
    database_url: str = Field(default="sqlite:///redishort.db")

    @validator("twitter_bearer_token")
    def validate_api_mode(cls, v, values):
        """
        Aprende: Validación cruzada de configuración
        - Si usas API oficial, DEBES tener bearer_token
        - Falla rápido al inicio, no en runtime
        """
        mode = values.get("twitter_source_mode")
        if mode == TwitterSourceMode.API_OFFICIAL and not v:
            raise ValueError(
                "twitter_bearer_token es requerido cuando twitter_source_mode=api_official"
            )
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Singleton global
settings = Settings()
```

**Aprende**:
- Enum para modos de acceso → Type-safe, autodocumentado
- Validación cruzada → Si mode=API, debe haber token
- Configuración de viralidad → Parametrizable, experimentable

### Paso 3: .env.example Documentado

```bash
# .env.example

# ============================================
# Twitter/X Configuration
# ============================================

# Modo de acceso a Twitter/X:
# - api_official: X API v2 oficial ($100-5000/mes)
# - scraping: Web scraping ético (gratis, zona gris legal)
# - third_party: Servicios como Apify ($50-200/mes)
TWITTER_SOURCE_MODE=scraping

# Si TWITTER_SOURCE_MODE=api_official:
# Obtén tu Bearer Token en: https://developer.twitter.com/en/portal/dashboard
# Costo mínimo: $100/mes (Basic tier)
# TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAxxxxxxxxxxxx

# Si TWITTER_SOURCE_MODE=scraping:
TWITTER_SCRAPING_USER_AGENT=RedishortBot/2.0 (Educational; +https://tu-url.com)
TWITTER_SCRAPING_DELAY_SEC=2.0

# Si TWITTER_SOURCE_MODE=third_party:
# APIFY_API_KEY=apify_api_xxxxxxxxxxxxx

# ============================================
# Viralidad Detection
# ============================================

# Umbrales para considerar un tweet "viral"
# Ajusta según tu nicho y audiencia objetivo
VIRALITY_MIN_LIKES=500
VIRALITY_MIN_RETWEETS=100
VIRALITY_MIN_REPLIES=50
VIRALITY_TIME_WINDOW_HOURS=24
VIRALITY_PREFERRED_LANGUAGE=es  # es=español, en=inglés

# ============================================
# Content Moderation
# ============================================

MODERATION_ENABLED=true
MODERATION_BLOCK_NSFW=true
MODERATION_BLOCK_HATE_SPEECH=true

# ============================================
# Google AI (Gemini)
# ============================================

# Obtén tu API key en: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX

# ============================================
# Text-to-Speech
# ============================================

TTS_PROVIDER=google_cloud  # google_cloud, elevenlabs
TTS_VOICE_SPANISH=es-ES-Studio-C
TTS_SPEAKING_RATE=1.1  # >1.0 = más rápido (sensacionalista)

# ============================================
# YouTube
# ============================================

YOUTUBE_CLIENT_SECRETS_FILE=client_secrets.json
YOUTUBE_DAILY_QUOTA=10000

# ============================================
# App Configuration
# ============================================

LOG_LEVEL=INFO
ENVIRONMENT=development
DATABASE_URL=sqlite:///redishort.db
```

### Paso 4: Logging Estructurado con Contexto de Fuente

```python
# src/redishort/observability/logging.py
import structlog
from ..config.settings import settings

def setup_logging():
    """
    Aprende: Logging estructurado con contexto global
    - Incluye source_mode en todos los logs
    - Facilita debugging de problemas de rate limiting
    - JSON en producción, pretty en desarrollo
    """
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    # Añade contexto global
    structlog.configure(
        processors=processors + [
            structlog.dev.ConsoleRenderer()  # Pretty print en dev
            if settings.environment == "development"
            else structlog.processors.JSONRenderer()  # JSON en prod
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Bind global context
    structlog.configure(
        context={
            "twitter_source_mode": settings.twitter_source_mode.value,
            "environment": settings.environment,
        }
    )

    return structlog.get_logger()

logger = setup_logging()
```

### Paso 5: Script de Validación de Acceso a Twitter

```python
# scripts/test_twitter_access.py
"""
Aprende: Validar acceso a Twitter al inicio del proyecto
- Evita descubrir problemas de API después de horas de desarrollo
- Fail-fast principle
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from redishort.config.settings import settings
from redishort.observability.logging import logger

def test_api_official():
    """Test X API v2 oficial"""
    import requests

    headers = {
        "Authorization": f"Bearer {settings.twitter_bearer_token.get_secret_value()}"
    }

    # Simple user lookup
    response = requests.get(
        "https://api.twitter.com/2/users/by/username/elonmusk",
        headers=headers
    )

    if response.status_code == 200:
        logger.info("api_official_success", data=response.json())
        return True
    else:
        logger.error("api_official_failed", status=response.status_code, error=response.text)
        return False

def test_scraping():
    """Test web scraping básico"""
    import requests
    from bs4 import BeautifulSoup
    import time

    headers = {
        "User-Agent": settings.twitter_scraping_user_agent
    }

    # Test simple: cargar página pública
    response = requests.get(
        "https://twitter.com/elonmusk",
        headers=headers
    )

    time.sleep(settings.twitter_scraping_delay_sec)

    if response.status_code == 200:
        logger.info("scraping_success", page_length=len(response.text))
        return True
    else:
        logger.error("scraping_failed", status=response.status_code)
        return False

def test_third_party():
    """Test third-party service (Apify)"""
    # Implementar según servicio elegido
    logger.warning("third_party_test_not_implemented")
    return False

def main():
    logger.info("testing_twitter_access", mode=settings.twitter_source_mode)

    if settings.twitter_source_mode == "api_official":
        success = test_api_official()
    elif settings.twitter_source_mode == "scraping":
        success = test_scraping()
    elif settings.twitter_source_mode == "third_party":
        success = test_third_party()

    if success:
        logger.info("twitter_access_validated", mode=settings.twitter_source_mode)
        sys.exit(0)
    else:
        logger.error("twitter_access_failed", mode=settings.twitter_source_mode)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

**Aprende**: Script de validación temprana
- Ejecuta ANTES de empezar desarrollo
- Detecta problemas de configuración/credenciales
- Documenta qué modo funciona

## ✅ Criterios de Éxito (Fase 0)

- [ ] Proyecto inicializado con Poetry
- [ ] Settings con validación de modos de X funcionando
- [ ] Script `test_twitter_access.py` ejecuta exitosamente
- [ ] `.env.example` completamente documentado
- [ ] Logging estructurado configurado
- [ ] `ruff`, `mypy`, `pre-commit` configurados
- [ ] README con sección "Opciones de Acceso a Twitter/X"

## 📖 Recursos de Aprendizaje

- [X API v2 Documentation](https://developer.twitter.com/en/docs/twitter-api)
- [X API Pricing](https://developer.twitter.com/en/portal/products)
- [Web Scraping Ethics](https://www.scrapehero.com/web-scraping-ethics/)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

---

# 🏗️ Fase 1: Core Architecture - Domain Models (2 semanas)

## Objetivos de Aprendizaje

- Diseñar domain models específicos para tweets
- Implementar scoring de viralidad
- Crear sistema de moderación de contenido
- Repository pattern para tweets y videos

## Conceptos Clave a Estudiar

| Concepto | Por Qué | Aplicación |
|----------|---------|------------|
| **Value Objects** | Encapsulan lógica de negocio | `ViralityScore`, `TweetMetrics` |
| **Domain Events** | Rastrean cambios importantes | `TweetFetchedEvent`, `VideoGeneratedEvent` |
| **Business Rules** | Lógica en domain, no en services | `is_suitable_for_video()`, `calculate_virality_score()` |

## Implementación Práctica

### Paso 1: Domain Models para Tweets

```python
# src/redishort/domain/models.py
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
from enum import Enum

class TweetLanguage(Enum):
    """
    Aprende: Enum para idiomas
    - Español es target primario (menos competencia)
    - Inglés como fallback
    """
    SPANISH = "es"
    ENGLISH = "en"
    PORTUGUESE = "pt"
    UNKNOWN = "unknown"

@dataclass(frozen=True)
class TweetMetrics:
    """
    Aprende: Value Object para métricas de engagement
    - Inmutable (frozen=True)
    - Encapsula cálculos relacionados con engagement
    - No es una entidad (no tiene ID propio)
    """
    likes: int
    retweets: int
    replies: int
    views: Optional[int] = None
    bookmarks: Optional[int] = None

    def total_engagement(self) -> int:
        """
        Aprende: Business logic en value objects
        - Engagement total = suma ponderada de interacciones
        - Replies valen más (indican controversia)
        """
        return (
            self.likes +
            (self.retweets * 2) +  # Retweets valen más (amplificación)
            (self.replies * 3)      # Replies valen más (engagement profundo)
        )

    def engagement_rate(self) -> float:
        """
        Tasa de engagement si tenemos views
        """
        if not self.views or self.views == 0:
            return 0.0
        return self.total_engagement() / self.views

@dataclass(frozen=True)
class ViralityScore:
    """
    Aprende: Value Object complejo para scoring de viralidad
    - Combina múltiples factores
    - Normalizado 0-100
    - Explicable (debug_info)
    """
    score: float  # 0-100
    recency_score: float  # 0-100 (más reciente = mejor)
    engagement_score: float  # 0-100
    velocity_score: float  # 0-100 (qué tan rápido crece)
    language_bonus: float  # 0-20 (español +20 puntos)

    @property
    def is_viral(self) -> bool:
        """
        Aprende: Business rule en value object
        - Score >70 = viral
        - Threshold experimentable
        """
        return self.score >= 70

    def debug_info(self) -> dict:
        """Para debugging y tuning del algoritmo"""
        return {
            "score": self.score,
            "breakdown": {
                "recency": self.recency_score,
                "engagement": self.engagement_score,
                "velocity": self.velocity_score,
                "language_bonus": self.language_bonus,
            }
        }

@dataclass(frozen=True)
class ViralTweet:
    """
    Aprende: Entity (tiene identidad: tweet_id)
    - Inmutable después de creación
    - Toda la lógica de negocio relacionada con tweets virales
    - No depende de APIs externas (puro dominio)
    """
    tweet_id: str
    author_username: str
    author_display_name: str
    text: str
    created_at: datetime
    metrics: TweetMetrics
    language: TweetLanguage
    url: str
    fetched_at: datetime = field(default_factory=datetime.utcnow)

    # Optional fields
    author_verified: bool = False
    author_followers: Optional[int] = None
    possibly_sensitive: bool = False
    reply_to_tweet_id: Optional[str] = None

    def calculate_virality_score(self) -> ViralityScore:
        """
        Aprende: Algoritmo de scoring de viralidad
        - Múltiples factores ponderados
        - Experimentable (ajustar pesos)
        - Documentado (por qué cada factor)
        """
        # 1. Recency (más reciente = mejor)
        hours_old = (datetime.utcnow() - self.created_at).total_seconds() / 3600
        recency_score = max(0, 100 - (hours_old * 2))  # -2 puntos por hora

        # 2. Engagement (normalizado a 0-100)
        engagement = self.metrics.total_engagement()
        # Log scale para normalizar (viral tweets tienen 100k+ engagement)
        import math
        engagement_score = min(100, (math.log10(max(1, engagement)) / 6) * 100)

        # 3. Velocity (engagement por hora desde publicación)
        velocity = engagement / max(1, hours_old)
        velocity_score = min(100, (math.log10(max(1, velocity)) / 4) * 100)

        # 4. Language bonus (español prioritario)
        language_bonus = 20 if self.language == TweetLanguage.SPANISH else 0

        # Score final (promedio ponderado + bonus)
        score = (
            recency_score * 0.2 +
            engagement_score * 0.4 +
            velocity_score * 0.4 +
            language_bonus
        )

        return ViralityScore(
            score=min(100, score),
            recency_score=recency_score,
            engagement_score=engagement_score,
            velocity_score=velocity_score,
            language_bonus=language_bonus
        )

    def is_suitable_for_video(self) -> bool:
        """
        Aprende: Business rules específicas del dominio
        - Texto no muy largo (legible en video)
        - No es reply (preferimos threads originales)
        - No es contenido sensible
        - Pasa threshold de viralidad
        """
        virality = self.calculate_virality_score()

        return (
            len(self.text) >= 20 and          # No demasiado corto
            len(self.text) <= 280 and         # Límite de Twitter
            not self.possibly_sensitive and   # No NSFW
            not self.reply_to_tweet_id and    # No replies, solo originales
            virality.is_viral                 # Pasa threshold de viralidad
        )

    def to_video_title(self) -> str:
        """
        Aprende: Transformación de dominio para UI
        - Genera título clickbait pero honesto
        - Trunca si es muy largo
        """
        # Hook sensacionalista
        hooks = [
            "🔥 Este tweet explotó Twitter:",
            "💥 Mira lo que dijo y se armó la grande:",
            "😱 Este tweet tiene a todos hablando:",
            "🚨 Twitter está que arde con esto:",
        ]

        import random
        hook = random.choice(hooks)

        # Truncar texto para título
        preview = self.text[:60] + "..." if len(self.text) > 60 else self.text

        return f"{hook} {preview}"

@dataclass
class VideoScript:
    """
    Aprende: Value Object para script generado
    - Segmentado (intro, body, outro)
    - Duración estimada
    """
    tweet_id: str
    hook: str                    # "Este tweet explotó con 50K likes..."
    tweet_context: str           # Contexto del tweet
    tweet_citation: str          # Cita del tweet (paráfrasis)
    engagement_mention: str      # "Tiene 50K likes, 10K RTs..."
    outro_cta: str              # "¿Tú qué opinas? Comenta abajo"
    total_duration_sec: float

    def to_segments(self) -> list[str]:
        """
        Aprende: Segmentación para TTS
        - Cada segmento = 1 audio clip
        - Facilita composición de video
        """
        return [
            self.hook,
            self.tweet_context,
            self.tweet_citation,
            self.engagement_mention,
            self.outro_cta
        ]

class VideoStatus(Enum):
    PENDING = "pending"
    GENERATING = "generating"
    GENERATED = "generated"
    UPLOADING = "uploading"
    UPLOADED = "uploaded"
    FAILED = "failed"

@dataclass
class GeneratedVideo:
    """Entity: Video generado de un tweet viral"""
    id: str
    tweet_id: str
    video_path: str
    thumbnail_path: Optional[str]
    status: VideoStatus
    title: str
    description: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    uploaded_at: Optional[datetime] = None
    youtube_id: Optional[str] = None
    youtube_url: Optional[str] = None

    def mark_as_uploaded(self, youtube_id: str) -> None:
        """
        Aprende: Métodos que mantienen invariantes
        - Estado siempre válido
        - No puedes marcar uploaded sin youtube_id
        """
        self.status = VideoStatus.UPLOADED
        self.youtube_id = youtube_id
        self.youtube_url = f"https://youtube.com/shorts/{youtube_id}"
        self.uploaded_at = datetime.utcnow()
```

**Aprende**:
- `ViralTweet` es la entidad central del dominio
- `calculate_virality_score()` es el corazón del negocio
- Lógica completamente testeable sin dependencias externas
- Algoritmo de scoring es experimentable (ajustar pesos)

### Paso 2: Content Moderator (Business Logic)

```python
# src/redishort/core/content_moderator.py
import re
from typing import Optional
import structlog
from ..domain.models import ViralTweet
from ..config.settings import settings

logger = structlog.get_logger()

class ModerationResult:
    """
    Aprende: Value Object para resultados de moderación
    - Explicable (por qué fue bloqueado)
    - Auditable
    """
    def __init__(self, approved: bool, reason: Optional[str] = None):
        self.approved = approved
        self.reason = reason

    def __bool__(self):
        return self.approved

class ContentModerator:
    """
    Aprende: Domain Service para moderación
    - No es una entidad (no tiene identidad)
    - Encapsula lógica de negocio compleja
    - Configurable via settings
    """

    # Palabras clave que indican contenido problemático
    HATE_SPEECH_KEYWORDS = {
        "es": ["puto", "puta", "marica", "negro de mierda"],  # Ejemplos, lista más exhaustiva en producción
        "en": ["nigger", "faggot", "retard"]
    }

    NSFW_KEYWORDS = {
        "es": ["porno", "xxx", "desnudo", "pack"],
        "en": ["porn", "xxx", "nude", "onlyfans"]
    }

    def __init__(self):
        self.logger = logger.bind(component="content_moderator")

    def moderate(self, tweet: ViralTweet) -> ModerationResult:
        """
        Aprende: Moderación multi-paso
        1. Flags de la plataforma (possibly_sensitive)
        2. Keywords de hate speech
        3. Keywords NSFW
        4. Patrones sospechosos (muchos @, links acortados)
        """
        if not settings.moderation_enabled:
            return ModerationResult(approved=True)

        # 1. Flag de Twitter
        if tweet.possibly_sensitive:
            return ModerationResult(
                approved=False,
                reason="marked_as_sensitive_by_twitter"
            )

        # 2. Hate speech
        if settings.moderation_block_hate_speech:
            if self._contains_hate_speech(tweet.text, tweet.language):
                return ModerationResult(
                    approved=False,
                    reason="hate_speech_detected"
                )

        # 3. NSFW
        if settings.moderation_block_nsfw:
            if self._contains_nsfw(tweet.text, tweet.language):
                return ModerationResult(
                    approved=False,
                    reason="nsfw_content_detected"
                )

        # 4. Spam patterns
        if self._is_likely_spam(tweet.text):
            return ModerationResult(
                approved=False,
                reason="spam_pattern_detected"
            )

        return ModerationResult(approved=True)

    def _contains_hate_speech(self, text: str, language) -> bool:
        """
        Aprende: Detección básica de hate speech
        - Keywords por idioma
        - Case-insensitive
        - Word boundaries (no false positives)
        """
        keywords = self.HATE_SPEECH_KEYWORDS.get(language.value, [])
        text_lower = text.lower()

        for keyword in keywords:
            # Use word boundaries to avoid false positives
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, text_lower):
                self.logger.warning("hate_speech_detected", keyword=keyword)
                return True

        return False

    def _contains_nsfw(self, text: str, language) -> bool:
        """Similar a hate_speech pero para NSFW"""
        keywords = self.NSFW_KEYWORDS.get(language.value, [])
        text_lower = text.lower()

        for keyword in keywords:
            if keyword in text_lower:
                self.logger.warning("nsfw_detected", keyword=keyword)
                return True

        return False

    def _is_likely_spam(self, text: str) -> bool:
        """
        Aprende: Heurísticas para spam
        - Muchos @ (más de 5)
        - Muchos hashtags (más de 8)
        - Links acortados sospechosos
        """
        # Contar @mentions
        mentions = len(re.findall(r'@\w+', text))
        if mentions > 5:
            return True

        # Contar hashtags
        hashtags = len(re.findall(r'#\w+', text))
        if hashtags > 8:
            return True

        # Links sospechosos
        suspicious_domains = ['bit.ly', 't.co', 'goo.gl', 'tinyurl.com']
        for domain in suspicious_domains:
            if domain in text and text.count('http') > 2:
                return True

        return False
```

### Paso 3: Repository Interfaces

```python
# src/redishort/domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from .models import ViralTweet, GeneratedVideo, VideoStatus, TweetLanguage

class TweetRepository(ABC):
    """
    Aprende: Interface para persistencia de tweets
    - Define QUÉ, no CÓMO
    - Permite múltiples implementaciones (SQLite, Postgres, Mock)
    """

    @abstractmethod
    def save(self, tweet: ViralTweet) -> None:
        """Guardar tweet en DB"""
        pass

    @abstractmethod
    def get_by_id(self, tweet_id: str) -> Optional[ViralTweet]:
        """Obtener tweet por ID"""
        pass

    @abstractmethod
    def get_unprocessed_viral_tweets(
        self,
        min_virality_score: float = 70,
        language: Optional[TweetLanguage] = None,
        limit: int = 10
    ) -> List[ViralTweet]:
        """
        Aprende: Query específica del dominio
        - Tweets con score >70
        - Opcionalmente filtrados por idioma
        - No procesados aún (no tienen video)
        """
        pass

    @abstractmethod
    def mark_as_processed(self, tweet_id: str) -> None:
        """Marcar tweet como procesado"""
        pass

    @abstractmethod
    def get_recent_viral_tweets(
        self,
        hours: int = 24,
        language: Optional[TweetLanguage] = None
    ) -> List[ViralTweet]:
        """Tweets virales de las últimas N horas"""
        pass

class VideoRepository(ABC):
    """Repository para videos generados"""

    @abstractmethod
    def save(self, video: GeneratedVideo) -> None:
        pass

    @abstractmethod
    def get_by_id(self, video_id: str) -> Optional[GeneratedVideo]:
        pass

    @abstractmethod
    def get_by_status(self, status: VideoStatus) -> List[GeneratedVideo]:
        pass

    @abstractmethod
    def update_status(self, video_id: str, status: VideoStatus) -> None:
        pass

    @abstractmethod
    def get_by_tweet_id(self, tweet_id: str) -> Optional[GeneratedVideo]:
        """Verificar si un tweet ya tiene video"""
        pass
```

### Paso 4: Testing de Domain Models

```python
# tests/unit/test_viral_tweet.py
import pytest
from datetime import datetime, timedelta
from redishort.domain.models import (
    ViralTweet, TweetMetrics, TweetLanguage, ViralityScore
)

def test_tweet_metrics_total_engagement():
    """Test cálculo de engagement total"""
    metrics = TweetMetrics(
        likes=1000,
        retweets=200,
        replies=50
    )

    # 1000 + (200*2) + (50*3) = 1000 + 400 + 150 = 1550
    assert metrics.total_engagement() == 1550


def test_virality_score_calculation_recent_high_engagement():
    """
    Aprende: Test de algoritmo de viralidad
    - Tweet reciente (1 hora) + alto engagement = score alto
    """
    tweet = ViralTweet(
        tweet_id="123",
        author_username="user",
        author_display_name="User",
        text="Este es un tweet viral de prueba",
        created_at=datetime.utcnow() - timedelta(hours=1),  # Muy reciente
        metrics=TweetMetrics(
            likes=10000,
            retweets=2000,
            replies=500
        ),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/123"
    )

    score = tweet.calculate_virality_score()

    # Debe ser viral (>70)
    assert score.is_viral
    assert score.score > 70

    # Debe tener language bonus
    assert score.language_bonus == 20


def test_virality_score_old_tweet_low_score():
    """Tweet antiguo (48 horas) debe tener score bajo"""
    tweet = ViralTweet(
        tweet_id="124",
        author_username="user",
        author_display_name="User",
        text="Tweet antiguo",
        created_at=datetime.utcnow() - timedelta(hours=48),  # Muy viejo
        metrics=TweetMetrics(likes=100, retweets=10, replies=5),
        language=TweetLanguage.ENGLISH,
        url="https://twitter.com/user/status/124"
    )

    score = tweet.calculate_virality_score()

    # No debe ser viral
    assert not score.is_viral
    assert score.recency_score < 10  # Muy viejo


def test_is_suitable_for_video():
    """
    Aprende: Test de business rules
    - Tweet debe cumplir múltiples criterios
    """
    # Tweet APTO
    good_tweet = ViralTweet(
        tweet_id="125",
        author_username="user",
        author_display_name="User",
        text="Este es un tweet perfecto para video, tiene buen largo y es viral",
        created_at=datetime.utcnow() - timedelta(minutes=30),
        metrics=TweetMetrics(likes=15000, retweets=3000, replies=800),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/125",
        possibly_sensitive=False,
        reply_to_tweet_id=None
    )

    assert good_tweet.is_suitable_for_video()

    # Tweet NO APTO: es reply
    reply_tweet = ViralTweet(
        tweet_id="126",
        author_username="user",
        author_display_name="User",
        text="Este es un reply",
        created_at=datetime.utcnow(),
        metrics=TweetMetrics(likes=10000, retweets=2000, replies=500),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/126",
        reply_to_tweet_id="999"  # Es reply
    )

    assert not reply_tweet.is_suitable_for_video()

    # Tweet NO APTO: contenido sensible
    sensitive_tweet = ViralTweet(
        tweet_id="127",
        author_username="user",
        author_display_name="User",
        text="Tweet sensible",
        created_at=datetime.utcnow(),
        metrics=TweetMetrics(likes=10000, retweets=2000, replies=500),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/127",
        possibly_sensitive=True  # Marcado como sensible
    )

    assert not sensitive_tweet.is_suitable_for_video()


def test_to_video_title():
    """Test generación de título clickbait"""
    tweet = ViralTweet(
        tweet_id="128",
        author_username="user",
        author_display_name="User",
        text="Esta es una opinión muy controversial que generó debate",
        created_at=datetime.utcnow(),
        metrics=TweetMetrics(likes=5000, retweets=1000, replies=300),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/128"
    )

    title = tweet.to_video_title()

    # Debe contener emoji y preview del tweet
    assert any(emoji in title for emoji in ["🔥", "💥", "😱", "🚨"])
    assert "Esta es una opinión muy controversial" in title


# tests/unit/test_content_moderator.py
from redishort.core.content_moderator import ContentModerator
from redishort.domain.models import ViralTweet, TweetMetrics, TweetLanguage

def test_moderator_blocks_hate_speech():
    """
    Aprende: Test de moderación
    - Debe bloquear contenido con hate speech
    """
    moderator = ContentModerator()

    tweet = ViralTweet(
        tweet_id="bad1",
        author_username="user",
        author_display_name="User",
        text="Este tweet contiene puto lenguaje ofensivo",
        created_at=datetime.utcnow(),
        metrics=TweetMetrics(likes=100, retweets=10, replies=5),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/bad1"
    )

    result = moderator.moderate(tweet)

    assert not result.approved
    assert result.reason == "hate_speech_detected"


def test_moderator_approves_clean_content():
    """Contenido limpio debe pasar moderación"""
    moderator = ContentModerator()

    tweet = ViralTweet(
        tweet_id="good1",
        author_username="user",
        author_display_name="User",
        text="Este tweet es completamente apropiado y positivo",
        created_at=datetime.utcnow(),
        metrics=TweetMetrics(likes=1000, retweets=100, replies=50),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/user/status/good1"
    )

    result = moderator.moderate(tweet)

    assert result.approved
    assert result.reason is None
```

**Aprende**:
- Tests de domain models son rápidos (sin I/O)
- Cada business rule tiene su test
- Fácil ajustar algoritmo de viralidad experimentando con tests

## ✅ Criterios de Éxito (Fase 1)

- [ ] Domain models (`ViralTweet`, `VideoScript`, `GeneratedVideo`) definidos
- [ ] `calculate_virality_score()` implementado y testeado
- [ ] `ContentModerator` funcionando con keywords en español
- [ ] Repository interfaces definidas
- [ ] Tests unitarios con >85% coverage en domain layer
- [ ] `mypy` pasa sin errores (type hints completos)

## 📖 Recursos de Aprendizaje

- [Domain-Driven Design Distilled](https://www.amazon.com/Domain-Driven-Design-Distilled-Vaughn-Vernon/dp/0134434420)
- [Value Objects Explained](https://martinfowler.com/bliki/ValueObject.html)
- [Cosmic Python - Domain Modeling](https://www.cosmicpython.com/book/chapter_01_domain_model.html)

---

# 🔌 Fase 2: Twitter/X Adapter + Viralidad Detection (2 semanas)

## Objetivos de Aprendizaje

- Implementar múltiples estrategias de acceso a X (API/Scraping)
- Rate limiting robusto y circuit breakers
- Detección de viralidad en tiempo real
- Manejo ético de datos de terceros

## Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **Strategy Pattern** | Múltiples formas de acceder a X | `TwitterAPIStrategy`, `TwitterScrapingStrategy` |
| **Rate Limiting Adaptativo** | X API tiene límites estrictos | `tenacity` + backoff exponencial |
| **Circuit Breaker** | Si X está caído, no saturar | `pybreaker` |
| **Ethical Scraping** | Respetar robots.txt, delays | `delays`, `User-Agent`, `respectful patterns` |

## Implementación Práctica

### Paso 1: Twitter Adapter con Strategy Pattern

```python
# src/redishort/adapters/twitter_adapter.py
from abc import ABC, abstractmethod
from typing import List, Protocol
import structlog
from ..domain.models import ViralTweet, TweetLanguage
from ..config.settings import settings

logger = structlog.get_logger()

class TwitterStrategy(Protocol):
    """
    Aprende: Protocol para estrategias de acceso a Twitter
    - Permite múltiples implementaciones
    - No requiere herencia (duck typing)
    """
    def fetch_trending_tweets(
        self,
        language: TweetLanguage,
        limit: int
    ) -> List[ViralTweet]:
        ...

    def fetch_tweet_by_id(self, tweet_id: str) -> ViralTweet:
        ...

class TwitterAdapter:
    """
    Aprende: Adapter con strategy pattern
    - Selecciona estrategia según configuración
    - Misma interface, múltiples implementaciones
    """

    def __init__(self):
        self.logger = logger.bind(adapter="twitter")

        # Factory: selecciona estrategia según config
        if settings.twitter_source_mode == "api_official":
            from .twitter_api_strategy import TwitterAPIStrategy
            self.strategy: TwitterStrategy = TwitterAPIStrategy()
        elif settings.twitter_source_mode == "scraping":
            from .twitter_scraping_strategy import TwitterScrapingStrategy
            self.strategy = TwitterScrapingStrategy()
        elif settings.twitter_source_mode == "third_party":
            from .twitter_apify_strategy import TwitterApifyStrategy
            self.strategy = TwitterApifyStrategy()
        else:
            raise ValueError(f"Unknown twitter_source_mode: {settings.twitter_source_mode}")

        self.logger.info("twitter_adapter_initialized", strategy=type(self.strategy).__name__)

    def fetch_viral_tweets(
        self,
        language: TweetLanguage = TweetLanguage.SPANISH,
        limit: int = 50
    ) -> List[ViralTweet]:
        """
        Aprende: Delegación a estrategia
        - Adapter no sabe CÓMO se obtienen tweets
        - Solo coordina y agrega logging
        """
        self.logger.info("fetching_viral_tweets", language=language.value, limit=limit)

        try:
            tweets = self.strategy.fetch_trending_tweets(language, limit)

            # Filtrar por viralidad
            viral = [t for t in tweets if t.calculate_virality_score().is_viral]

            self.logger.info(
                "viral_tweets_fetched",
                total=len(tweets),
                viral=len(viral),
                viral_pct=len(viral)/len(tweets)*100 if tweets else 0
            )

            return viral

        except Exception as e:
            self.logger.error("fetch_failed", error=str(e))
            raise
```

### Paso 2: API Official Strategy (con Rate Limiting)

```python
# src/redishort/adapters/twitter_api_strategy.py
import tweepy
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from pybreaker import CircuitBreaker
from ratelimit import limits, sleep_and_retry
import structlog
from typing import List
from ..domain.models import ViralTweet, TweetMetrics, TweetLanguage
from ..config.settings import settings

logger = structlog.get_logger()

# Circuit breaker: Si 5 requests fallan, abre el circuito por 60 segundos
twitter_api_breaker = CircuitBreaker(
    fail_max=5,
    reset_timeout=60,
    name="twitter_api"
)

class TwitterAPIStrategy:
    """
    Aprende: Implementación con X API v2 oficial
    - Rate limiting estricto (50 req/15min en Basic tier)
    - Circuit breaker para fallos sistemáticos
    - Retry para fallos transitorios
    """

    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=settings.twitter_bearer_token.get_secret_value()
        )
        self.logger = logger.bind(strategy="api_official")

    @twitter_api_breaker
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=4, max=30),
        retry=retry_if_exception_type((tweepy.TweepyException, ConnectionError))
    )
    @sleep_and_retry
    @limits(calls=50, period=900)  # 50 calls per 15 minutes (API limit)
    def fetch_trending_tweets(
        self,
        language: TweetLanguage,
        limit: int = 50
    ) -> List[ViralTweet]:
        """
        Aprende: Triple capa de resiliencia
        1. @limits: Rate limiting (no exceder API quota)
        2. @retry: Reintentar errores transitorios
        3. @circuit_breaker: Dejar de intentar si API está caída

        Orden importa: limits → retry → circuit_breaker
        """
        try:
            self.logger.info("fetching_via_api", language=language.value, limit=limit)

            # Buscar tweets trending usando search_recent_tweets
            query = self._build_search_query(language)

            response = self.client.search_recent_tweets(
                query=query,
                max_results=min(limit, 100),  # API limit per request
                tweet_fields=[
                    'created_at', 'public_metrics', 'author_id',
                    'lang', 'possibly_sensitive', 'referenced_tweets'
                ],
                user_fields=['username', 'name', 'verified', 'public_metrics'],
                expansions=['author_id']
            )

            if not response.data:
                self.logger.warning("no_tweets_found")
                return []

            # Parse tweets
            tweets = self._parse_response(response, language)

            self.logger.info("tweets_fetched_via_api", count=len(tweets))
            return tweets

        except tweepy.TweepyException as e:
            self.logger.error("api_error", error=str(e), code=e.api_code if hasattr(e, 'api_code') else None)
            raise
        except Exception as e:
            self.logger.error("unexpected_error", error=str(e))
            raise

    def _build_search_query(self, language: TweetLanguage) -> str:
        """
        Aprende: Query building para X API
        - Filtra por idioma
        - Excluye retweets (queremos originales)
        - Excluye replies
        - Solo tweets con engagement alto
        """
        lang_code = language.value

        # Query: idioma + no RT + no replies + engagement mínimo
        query = f"lang:{lang_code} -is:retweet -is:reply min_faves:{settings.virality_min_likes}"

        # Opcional: filtrar por palabras clave de nichos populares
        # query += " (futbol OR drama OR confesion OR polemica)"

        return query

    def _parse_response(self, response, language: TweetLanguage) -> List[ViralTweet]:
        """
        Aprende: Parsing de respuesta de API
        - Transformar formato de X API a nuestro domain model
        - Manejo de datos opcionales (None-safe)
        """
        tweets = []

        # Create user lookup dict
        users = {user.id: user for user in response.includes.get('users', [])}

        for tweet_data in response.data:
            author = users.get(tweet_data.author_id)
            if not author:
                continue

            # Parse referenced_tweets para detectar replies
            referenced = tweet_data.referenced_tweets or []
            reply_to = next(
                (ref.id for ref in referenced if ref.type == 'replied_to'),
                None
            )

            tweet = ViralTweet(
                tweet_id=tweet_data.id,
                author_username=author.username,
                author_display_name=author.name,
                text=tweet_data.text,
                created_at=tweet_data.created_at,
                metrics=TweetMetrics(
                    likes=tweet_data.public_metrics['like_count'],
                    retweets=tweet_data.public_metrics['retweet_count'],
                    replies=tweet_data.public_metrics['reply_count'],
                    views=tweet_data.public_metrics.get('impression_count')
                ),
                language=language,
                url=f"https://twitter.com/{author.username}/status/{tweet_data.id}",
                author_verified=author.verified or False,
                author_followers=author.public_metrics.get('followers_count'),
                possibly_sensitive=tweet_data.possibly_sensitive or False,
                reply_to_tweet_id=reply_to
            )

            tweets.append(tweet)

        return tweets

    def fetch_tweet_by_id(self, tweet_id: str) -> ViralTweet:
        """Fetch single tweet by ID"""
        # Similar implementation...
        pass
```

### Paso 3: Scraping Strategy (Alternativa Pragmática)

```python
# src/redishort/adapters/twitter_scraping_strategy.py
import requests
from bs4 import BeautifulSoup
import time
import re
from typing import List, Optional
from pybreaker import CircuitBreaker
from tenacity import retry, stop_after_attempt, wait_exponential
import structlog
from ..domain.models import ViralTweet, TweetMetrics, TweetLanguage
from ..config.settings import settings

logger = structlog.get_logger()

scraping_breaker = CircuitBreaker(fail_max=3, reset_timeout=120, name="scraping")

class TwitterScrapingStrategy:
    """
    Aprende: Web scraping ético
    - Respeta robots.txt (en teoría, X lo bloquea todo)
    - Delays entre requests
    - User-Agent honesto
    - Zona gris legal: úsalo para aprendizaje, migra a API oficial en producción

    IMPORTANTE: Twitter puede cambiar HTML en cualquier momento (frágil)
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': settings.twitter_scraping_user_agent,
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        })
        self.logger = logger.bind(strategy="scraping")
        self.logger.warning("scraping_strategy_active", warning="Use API oficial en producción")

    @scraping_breaker
    @retry(
        stop=stop_after_attempt(2),
        wait=wait_exponential(multiplier=2, min=3, max=15)
    )
    def fetch_trending_tweets(
        self,
        language: TweetLanguage,
        limit: int = 50
    ) -> List[ViralTweet]:
        """
        Aprende: Scraping de trending topics
        - Alternativa cuando API es muy cara
        - FRÁGIL: Twitter cambia HTML frecuentemente
        - RIESGOSO: Puede resultar en ban de IP

        Estrategia:
        1. Usar endpoints públicos (trending, search)
        2. Parsear HTML con BeautifulSoup
        3. Delays agresivos para no ser baneado
        """
        self.logger.warning("using_scraping", note="Consider API oficial para producción")

        # Para español, usar trending de país hispanohablante
        country_codes = {
            TweetLanguage.SPANISH: ["es", "mx", "ar", "co"],  # España, México, Argentina, Colombia
            TweetLanguage.ENGLISH: ["us", "gb"],
        }

        tweets = []
        countries = country_codes.get(language, ["us"])

        for country in countries:
            country_tweets = self._scrape_trending_from_country(country, language)
            tweets.extend(country_tweets)

            # Delay ético entre countries
            time.sleep(settings.twitter_scraping_delay_sec)

            if len(tweets) >= limit:
                break

        return tweets[:limit]

    def _scrape_trending_from_country(
        self,
        country_code: str,
        language: TweetLanguage
    ) -> List[ViralTweet]:
        """
        Aprende: Scraping de trending topics de un país

        NOTA: Este es un ejemplo simplificado.
        En producción, considera usar librerías especializadas:
        - snscrape (más robusta pero también en zona gris)
        - nitter instances (frontend alternativo de Twitter)
        """
        url = f"https://twitter.com/explore/tabs/trending"

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            # Delay ético
            time.sleep(settings.twitter_scraping_delay_sec)

            # Parse HTML (MUY frágil, Twitter usa JS rendering)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar tweets en trending
            # NOTA: Este selector es PLACEHOLDER, Twitter usa JS rendering dinámico
            # En realidad necesitarías Selenium o Playwright para renderizar JS

            self.logger.warning(
                "scraping_html_parse",
                warning="Twitter usa JS rendering, este approach es limitado"
            )

            # TODO: Implementar con Selenium/Playwright para JS rendering
            # Por ahora, retornar lista vacía como placeholder

            return []

        except requests.RequestException as e:
            self.logger.error("scraping_request_failed", error=str(e))
            return []

    def fetch_tweet_by_id(self, tweet_id: str) -> ViralTweet:
        """
        Fetch single tweet via scraping

        Aprende: Alternativa más viable que trending
        - URL directa: https://twitter.com/user/status/{tweet_id}
        - No requiere autenticación para tweets públicos
        - Usa nitter como fallback (frontend alternativo)
        """
        # Try nitter first (más confiable para scraping)
        nitter_instances = [
            "nitter.net",
            "nitter.42l.fr",
            "nitter.pussthecat.org"
        ]

        for instance in nitter_instances:
            try:
                tweet = self._scrape_from_nitter(instance, tweet_id)
                if tweet:
                    return tweet
            except Exception as e:
                self.logger.warning("nitter_instance_failed", instance=instance, error=str(e))
                continue

        raise ValueError(f"Failed to scrape tweet {tweet_id} from all sources")

    def _scrape_from_nitter(self, instance: str, tweet_id: str) -> Optional[ViralTweet]:
        """
        Aprende: Nitter como alternativa de scraping
        - Nitter es un frontend alternativo de Twitter
        - HTML más simple (no JS rendering)
        - Rate limits más relajados
        - Proyecto open-source
        """
        url = f"https://{instance}/i/status/{tweet_id}"

        response = self.session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse Nitter HTML (más estable que Twitter directo)
        # TODO: Implementar parseo completo de Nitter HTML

        time.sleep(settings.twitter_scraping_delay_sec)

        return None  # Placeholder
```

**Aprende**:
- Scraping es FRÁGIL (HTML cambia constantemente)
- X usa JS rendering (necesitas Selenium/Playwright)
- Nitter es alternativa más viable para scraping
- **Recomendación**: Úsalo para prototipo, migra a API oficial para producción

### Paso 4: Viralidad Detector Service

```python
# src/redishort/core/virality_detector.py
import structlog
from typing import List
from ..domain.models import ViralTweet, TweetLanguage
from ..domain.repositories import TweetRepository
from ..adapters.twitter_adapter import TwitterAdapter
from ..core.content_moderator import ContentModerator

logger = structlog.get_logger()

class ViralityDetector:
    """
    Aprende: Service Layer para detección de viralidad
    - Coordina: Twitter adapter + Content moderator + Repository
    - No contiene business logic (está en domain models)
    - Orquesta workflow
    """

    def __init__(
        self,
        twitter_adapter: TwitterAdapter,
        tweet_repo: TweetRepository,
        content_moderator: ContentModerator
    ):
        self.twitter = twitter_adapter
        self.tweet_repo = tweet_repo
        self.moderator = content_moderator
        self.logger = logger.bind(service="virality_detector")

    def detect_and_save_viral_tweets(
        self,
        language: TweetLanguage = TweetLanguage.SPANISH,
        limit: int = 50
    ) -> List[ViralTweet]:
        """
        Workflow completo:
        1. Fetch tweets de Twitter
        2. Calcular virality score
        3. Moderar contenido
        4. Guardar en DB
        5. Retornar tweets aptos

        Returns: Tweets virales aptos para video
        """
        self.logger.info("detecting_viral_tweets", language=language.value, limit=limit)

        # 1. Fetch from Twitter
        tweets = self.twitter.fetch_viral_tweets(language, limit)

        # 2. Filter + moderate
        suitable_tweets = []

        for tweet in tweets:
            # Calculate virality (ya filtrado en adapter, pero re-verificamos)
            virality = tweet.calculate_virality_score()

            if not virality.is_viral:
                self.logger.debug("tweet_not_viral", tweet_id=tweet.tweet_id, score=virality.score)
                continue

            # Moderate content
            moderation = self.moderator.moderate(tweet)
            if not moderation.approved:
                self.logger.warning(
                    "tweet_moderated",
                    tweet_id=tweet.tweet_id,
                    reason=moderation.reason
                )
                continue

            # Business rule: suitable for video
            if not tweet.is_suitable_for_video():
                self.logger.debug("tweet_not_suitable", tweet_id=tweet.tweet_id)
                continue

            # Save to DB
            self.tweet_repo.save(tweet)
            suitable_tweets.append(tweet)

            self.logger.info(
                "viral_tweet_saved",
                tweet_id=tweet.tweet_id,
                virality_score=virality.score,
                engagement=tweet.metrics.total_engagement()
            )

        self.logger.info(
            "viral_detection_complete",
            total_fetched=len(tweets),
            suitable=len(suitable_tweets),
            filtered_pct=(len(tweets)-len(suitable_tweets))/len(tweets)*100 if tweets else 0
        )

        return suitable_tweets
```

## ✅ Criterios de Éxito (Fase 2)

- [ ] `TwitterAdapter` con strategy pattern funcionando
- [ ] Al menos 1 estrategia implementada (API o scraping)
- [ ] Rate limiting probado (no excede límites de API)
- [ ] Circuit breaker se abre tras fallos consecutivos
- [ ] `ViralityDetector` service completo
- [ ] Integration tests con API real (en CI, solo si tienes creds)
- [ ] Logs estructurados de cada request

## 📖 Recursos de Aprendizaje

- [Tweepy Documentation](https://docs.tweepy.org/)
- [X API v2 Docs](https://developer.twitter.com/en/docs/twitter-api)
- [Web Scraping Best Practices](https://www.scrapehero.com/a-beginners-guide-to-web-scraping-best-practices/)
- [Nitter Project](https://github.com/zedeus/nitter)
- [tenacity Retry Library](https://tenacity.readthedocs.io/)

---

# 🎬 Fase 3: Video Generation Pipeline - Tweet Visualization (2 semanas)

## Objetivos de Aprendizaje

- Renderizar tweets como imágenes profesionales
- Composición de video con overlay de tweet
- Animaciones y efectos (emojis volando, counters subiendo)
- Pipeline optimizado (async TTS)

## Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **Tweet-to-Image** | Visualizar tweet como imagen estética | Pillow + templates |
| **Overlay Composition** | Tweet sobre video de fondo | MoviePy layers |
| **Animations** | Retención (emojis, counters) | After Effects o code |
| **Resource Management** | Evitar memory leaks | Context managers |

## Implementación Práctica

### Paso 1: Tweet Visualizer (Imagen del Tweet)

```python
# src/redishort/video/tweet_visualizer.py
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap
import structlog
from ..domain.models import ViralTweet

logger = structlog.get_logger()

class TweetVisualizer:
    """
    Aprende: Renderizar tweet como imagen profesional
    - Simula estilo de Twitter (fondo, fuente, layout)
    - Personalizable (colores, tamaños)
    - Output: PNG transparente para overlay
    """

    def __init__(self, assets_dir: Path, output_dir: Path):
        self.assets_dir = assets_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Load fonts
        self.font_bold = ImageFont.truetype(
            str(assets_dir / "fonts" / "Arial-Bold.ttf"),
            size=60
        )
        self.font_regular = ImageFont.truetype(
            str(assets_dir / "fonts" / "Arial.ttf"),
            size=50
        )
        self.font_username = ImageFont.truetype(
            str(assets_dir / "fonts" / "Arial.ttf"),
            size=40
        )

        self.logger = logger.bind(component="tweet_visualizer")

    def render_tweet(self, tweet: ViralTweet) -> Path:
        """
        Render tweet como imagen PNG

        Layout:
        ┌──────────────────────────┐
        │ @username                │
        │ Display Name        ✓    │
        │                          │
        │ Tweet text here...       │
        │ Can be multiple lines    │
        │                          │
        │ ❤️ 10K  🔁 2K  💬 500     │
        └──────────────────────────┘

        Returns: Path to PNG
        """
        self.logger.info("rendering_tweet", tweet_id=tweet.tweet_id)

        # Canvas size (9:16 aspect ratio para Shorts)
        width, height = 1080, 1920

        # Create image with rounded rect background
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Tweet card (centrado verticalmente)
        card_width = int(width * 0.9)  # 90% del ancho
        card_height = 800
        card_x = (width - card_width) // 2
        card_y = (height - card_height) // 2

        # Background rounded rectangle (blanco con opacidad)
        self._draw_rounded_rectangle(
            draw,
            [(card_x, card_y), (card_x + card_width, card_y + card_height)],
            radius=30,
            fill=(255, 255, 255, 240)  # Blanco semi-transparente
        )

        # Author section
        y_offset = card_y + 40

        # Display name (bold)
        display_name = tweet.author_display_name
        if tweet.author_verified:
            display_name += " ✓"

        draw.text(
            (card_x + 40, y_offset),
            display_name,
            fill=(15, 20, 25),  # Negro Twitter
            font=self.font_bold
        )

        y_offset += 70

        # Username (gris)
        draw.text(
            (card_x + 40, y_offset),
            f"@{tweet.author_username}",
            fill=(83, 100, 113),  # Gris Twitter
            font=self.font_username
        )

        y_offset += 80

        # Tweet text (wrapped)
        wrapped_text = textwrap.fill(tweet.text, width=35)  # ~35 chars per line
        draw.multiline_text(
            (card_x + 40, y_offset),
            wrapped_text,
            fill=(15, 20, 25),
            font=self.font_regular,
            spacing=10
        )

        # Metrics (bottom)
        y_offset = card_y + card_height - 100

        metrics_text = f"❤️ {self._format_number(tweet.metrics.likes)}  " \
                      f"🔁 {self._format_number(tweet.metrics.retweets)}  " \
                      f"💬 {self._format_number(tweet.metrics.replies)}"

        draw.text(
            (card_x + 40, y_offset),
            metrics_text,
            fill=(83, 100, 113),
            font=self.font_username
        )

        # Save
        output_path = self.output_dir / f"tweet_{tweet.tweet_id}.png"
        img.save(output_path, 'PNG')

        self.logger.info("tweet_rendered", path=str(output_path))
        return output_path

    def _draw_rounded_rectangle(self, draw, coords, radius, fill):
        """
        Aprende: Dibujar rectángulo con esquinas redondeadas
        - Pillow no tiene método nativo para esto
        - Componer arcos + líneas
        """
        x1, y1 = coords[0]
        x2, y2 = coords[1]

        # Draw rounded corners as circles
        draw.ellipse([x1, y1, x1 + radius * 2, y1 + radius * 2], fill=fill)
        draw.ellipse([x2 - radius * 2, y1, x2, y1 + radius * 2], fill=fill)
        draw.ellipse([x1, y2 - radius * 2, x1 + radius * 2, y2], fill=fill)
        draw.ellipse([x2 - radius * 2, y2 - radius * 2, x2, y2], fill=fill)

        # Draw rectangles to connect corners
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

    def _format_number(self, num: int) -> str:
        """
        Aprende: Formatear números para métricas
        - 1000 → 1K
        - 1500000 → 1.5M
        """
        if num >= 1_000_000:
            return f"{num / 1_000_000:.1f}M"
        elif num >= 1_000:
            return f"{num / 1_000:.1f}K"
        else:
            return str(num)
```

### Paso 2: Video Composer (Composición Final)

```python
# src/redishort/video/video_composer.py
from pathlib import Path
from contextlib import contextmanager
from moviepy.editor import (
    VideoFileClip, AudioFileClip, ImageClip,
    CompositeVideoClip, concatenate_videoclips, TextClip
)
import random
import structlog
from ..domain.models import VideoScript

logger = structlog.get_logger()

@contextmanager
def managed_clip(clip):
    """Context manager para cleanup de clips"""
    try:
        yield clip
    finally:
        if clip:
            clip.close()

class VideoComposer:
    """
    Aprende: Composición de video final
    - Background video (gaming, subway surfers, etc)
    - Tweet overlay (imagen del tweet)
    - Audio (TTS narración)
    - Animaciones opcionales (emojis, text overlays)
    """

    def __init__(self, assets_dir: Path, output_dir: Path):
        self.assets_dir = assets_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logger.bind(component="video_composer")

    def compose_video(
        self,
        script: VideoScript,
        tweet_image_path: Path,
        audio_paths: list[Path]
    ) -> Path:
        """
        Compose final video

        Layers (bottom to top):
        1. Background video (gameplay, etc)
        2. Tweet image overlay (centrado)
        3. Text overlays (captions si needed)

        Audio:
        - TTS narration

        Returns: Path to final MP4
        """
        output_path = self.output_dir / f"video_{script.tweet_id}.mp4"

        try:
            self.logger.info("composing_video", tweet_id=script.tweet_id)

            # 1. Load background
            with managed_clip(self._load_random_background()) as background:

                # 2. Load tweet image
                with managed_clip(ImageClip(str(tweet_image_path))) as tweet_img:

                    # 3. Concatenate audio segments
                    audio_clips = [AudioFileClip(str(p)) for p in audio_paths]
                    full_audio = concatenate_audioclips(audio_clips)
                    duration = full_audio.duration

                    # 4. Resize background to match duration
                    # Loop si es muy corto, crop si es muy largo
                    if background.duration < duration:
                        # Loop background
                        loops_needed = int(duration / background.duration) + 1
                        background = concatenate_videoclips([background] * loops_needed)

                    background = background.subclip(0, duration)

                    # 5. Position tweet image (centrado)
                    tweet_img = tweet_img.set_duration(duration)
                    tweet_img = tweet_img.set_position('center')

                    # 6. Composite layers
                    final = CompositeVideoClip([
                        background,
                        tweet_img
                    ])

                    # 7. Add audio
                    final = final.set_audio(full_audio)

                    # 8. Export
                    final.write_videofile(
                        str(output_path),
                        codec='libx264',
                        audio_codec='aac',
                        fps=30,
                        preset='medium',
                        threads=4
                    )

                    # Cleanup
                    for clip in audio_clips:
                        clip.close()
                    full_audio.close()
                    final.close()

            self.logger.info("video_composed", path=str(output_path), duration=duration)
            return output_path

        except Exception as e:
            self.logger.error("composition_failed", error=str(e))
            raise

    def _load_random_background(self) -> VideoFileClip:
        """
        Aprende: Background aleatorio
        - Variedad evita monotonía
        - Nichos populares: gameplay, subway surfers, satisfying videos
        """
        backgrounds = list(self.assets_dir.glob("backgrounds/*.mp4"))
        if not backgrounds:
            raise ValueError("No background videos found in assets/backgrounds/")

        bg_path = random.choice(backgrounds)
        self.logger.debug("background_selected", path=bg_path.name)

        return VideoFileClip(str(bg_path))
```

### Paso 3: Script Generator (Gemini para Narración)

```python
# src/redishort/adapters/gemini_script_generator.py
import google.generativeai as genai
from pybreaker import CircuitBreaker
from tenacity import retry, stop_after_attempt, wait_exponential
import structlog
from ..domain.models import ViralTweet, VideoScript
from ..config.settings import settings

logger = structlog.get_logger()

gemini_breaker = CircuitBreaker(fail_max=5, reset_timeout=60, name="gemini")

class GeminiScriptGenerator:
    """
    Aprende: Generación de script sensacionalista
    - Prompt engineering para tono viral
    - Segmentación para TTS
    """

    def __init__(self):
        genai.configure(api_key=settings.google_api_key.get_secret_value())

        self.safety_settings = {
            "HARM_CATEGORY_HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_HATE_SPEECH": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_MEDIUM_AND_ABOVE",
        }

        self.model = genai.GenerativeModel(
            'gemini-pro',
            safety_settings=self.safety_settings
        )

        self.logger = logger.bind(adapter="gemini_script")

    @gemini_breaker
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=4, max=30))
    def generate_script(self, tweet: ViralTweet) -> VideoScript:
        """
        Aprende: Prompt engineering para YouTube Shorts
        - Tono sensacionalista pero no exagerado
        - Hook fuerte (primeros 3 segundos)
        - CTA al final
        """
        prompt = self._build_prompt(tweet)

        self.logger.info("generating_script", tweet_id=tweet.tweet_id)

        try:
            response = self.model.generate_content(prompt)
            script_text = response.text

            # Parse segments
            segments = self._parse_script_segments(script_text)

            return VideoScript(
                tweet_id=tweet.tweet_id,
                hook=segments['hook'],
                tweet_context=segments['context'],
                tweet_citation=segments['citation'],
                engagement_mention=segments['engagement'],
                outro_cta=segments['cta'],
                total_duration_sec=len(segments) * 4.0  # ~4 sec per segment
            )

        except Exception as e:
            self.logger.error("script_generation_failed", error=str(e))
            raise

    def _build_prompt(self, tweet: ViralTweet) -> str:
        """
        Aprende: Prompt template para script viral
        """
        virality = tweet.calculate_virality_score()

        return f"""
Eres un guionista de YouTube Shorts viral en español. Tu objetivo es convertir este tweet viral en un video de 15-20 segundos que enganche y genere comentarios.

TWEET ORIGINAL:
Autor: @{tweet.author_username}
Texto: "{tweet.text}"
Engagement: {tweet.metrics.likes} likes, {tweet.metrics.retweets} retweets, {tweet.metrics.replies} replies

INSTRUCCIONES:
1. HOOK (3-4 segundos): Empieza con algo que enganche inmediatamente. Usa frases como:
   - "Mira lo que este usuario soltó en Twitter y se armó la grande..."
   - "Este tweet explotó con {tweet.metrics.likes} likes y no es para menos..."
   - "Twitter está que arde con esto que dijo @{tweet.author_username}..."

2. CONTEXTO (3-4 segundos): Muy breve contexto si es necesario (quién es, de qué va).

3. CITACIÓN (5-6 segundos): Cita o parafrasea el tweet. Hazlo natural, como si lo contaras a un amigo.

4. ENGAGEMENT (2-3 segundos): Menciona el engagement: "Tiene {tweet.metrics.likes} likes, {tweet.metrics.retweets} RTs..."

5. CTA (2-3 segundos): Cierra con pregunta abierta: "¿Tú qué opinas? Comenta abajo" o similar.

TONO:
- Energético, rápido, sensacionalista (pero honesto)
- Español neutro (evita regionalismos muy marcados)
- Como si le contaras chisme a un amigo

FORMATO DE SALIDA:
HOOK: [texto del hook]
CONTEXT: [texto del contexto]
CITATION: [texto de la citación]
ENGAGEMENT: [texto del engagement mention]
CTA: [texto del CTA]

GENERA EL SCRIPT:
"""

    def _parse_script_segments(self, script_text: str) -> dict:
        """Parse script en segmentos"""
        import re

        segments = {}

        patterns = {
            'hook': r'HOOK:\s*(.+?)(?=CONTEXT:|$)',
            'context': r'CONTEXT:\s*(.+?)(?=CITATION:|$)',
            'citation': r'CITATION:\s*(.+?)(?=ENGAGEMENT:|$)',
            'engagement': r'ENGAGEMENT:\s*(.+?)(?=CTA:|$)',
            'cta': r'CTA:\s*(.+?)(?=$)',
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, script_text, re.DOTALL | re.IGNORECASE)
            if match:
                segments[key] = match.group(1).strip()
            else:
                # Fallback
                segments[key] = ""

        return segments
```

### Paso 4: Full Pipeline Service

```python
# src/redishort/core/video_generation_service.py
import asyncio
from pathlib import Path
import structlog
from ..domain.models import ViralTweet, GeneratedVideo, VideoStatus
from ..domain.repositories import TweetRepository, VideoRepository
from ..adapters.gemini_script_generator import GeminiScriptGenerator
from ..adapters.tts_adapter import TTSAdapter
from ..video.tweet_visualizer import TweetVisualizer
from ..video.video_composer import VideoComposer

logger = structlog.get_logger()

class VideoGenerationService:
    """
    Aprende: Service layer orchestration
    - Coordina todo el pipeline
    - Async donde es beneficioso (TTS)
    - Error handling en cada paso
    """

    def __init__(
        self,
        tweet_repo: TweetRepository,
        video_repo: VideoRepository,
        script_generator: GeminiScriptGenerator,
        tts_adapter: TTSAdapter,
        tweet_visualizer: TweetVisualizer,
        video_composer: VideoComposer
    ):
        self.tweet_repo = tweet_repo
        self.video_repo = video_repo
        self.script_gen = script_generator
        self.tts = tts_adapter
        self.visualizer = tweet_visualizer
        self.composer = video_composer
        self.logger = logger.bind(service="video_generation")

    async def generate_video_from_tweet(self, tweet_id: str) -> GeneratedVideo:
        """
        Full pipeline:
        1. Get tweet from DB
        2. Generate script (Gemini)
        3. Generate audio (TTS async)
        4. Render tweet image
        5. Compose video
        6. Save to DB

        Returns: GeneratedVideo entity
        """
        tweet = self.tweet_repo.get_by_id(tweet_id)
        if not tweet:
            raise ValueError(f"Tweet {tweet_id} not found")

        # Create video entity
        video = GeneratedVideo(
            id=f"video_{tweet_id}",
            tweet_id=tweet_id,
            video_path="",
            thumbnail_path=None,
            status=VideoStatus.GENERATING,
            title=tweet.to_video_title(),
            description=self._generate_description(tweet)
        )
        self.video_repo.save(video)

        try:
            self.logger.info("starting_video_generation", tweet_id=tweet_id)

            # 1. Generate script
            self.logger.info("generating_script", tweet_id=tweet_id)
            script = self.script_gen.generate_script(tweet)

            # 2. Generate audio (async for all segments)
            self.logger.info("generating_audio", tweet_id=tweet_id)
            audio_paths = await self._generate_audio_async(script)

            # 3. Render tweet image
            self.logger.info("rendering_tweet_image", tweet_id=tweet_id)
            tweet_image = self.visualizer.render_tweet(tweet)

            # 4. Compose video
            self.logger.info("composing_video", tweet_id=tweet_id)
            video_path = self.composer.compose_video(script, tweet_image, audio_paths)

            # 5. Update video entity
            video.video_path = str(video_path)
            video.status = VideoStatus.GENERATED
            self.video_repo.save(video)

            # 6. Mark tweet as processed
            self.tweet_repo.mark_as_processed(tweet_id)

            self.logger.info("video_generated_successfully", video_id=video.id, path=str(video_path))
            return video

        except Exception as e:
            self.logger.error("video_generation_failed", tweet_id=tweet_id, error=str(e))
            video.status = VideoStatus.FAILED
            self.video_repo.save(video)
            raise

    async def _generate_audio_async(self, script) -> list[Path]:
        """
        Aprende: Generación paralela de audio
        - Todos los segmentos a la vez
        - 5x más rápido que secuencial
        """
        segments = script.to_segments()

        tasks = [
            asyncio.to_thread(
                self.tts.generate_audio,
                text=segment,
                output_path=self.tts.output_dir / f"{script.tweet_id}_seg{idx}.mp3"
            )
            for idx, segment in enumerate(segments)
        ]

        audio_paths = await asyncio.gather(*tasks)
        return list(audio_paths)

    def _generate_description(self, tweet: ViralTweet) -> str:
        """
        Aprende: Descripción de YouTube con atribución
        - SEO keywords
        - Atribución al tweet original (legal/ético)
        - CTA
        """
        return f"""
{tweet.text}

Tweet original de @{tweet.author_username}: {tweet.url}

Este video es una reacción/comentario al tweet viral mencionado. Todo el crédito del contenido original va a su autor.

¿Qué opinas? Deja tu comentario abajo 👇

#TwitterViral #Shorts #ReaccionTweet #{tweet.author_username}
""".strip()
```

## ✅ Criterios de Éxito (Fase 3)

- [ ] `TweetVisualizer` genera imágenes de tweets estéticas
- [ ] `VideoComposer` compone video final con background + tweet + audio
- [ ] `GeminiScriptGenerator` genera scripts sensacionalistas en español
- [ ] Pipeline completo genera video de tweet en <2 minutos
- [ ] No memory leaks (verificar con `memory_profiler`)
- [ ] Videos de calidad (30fps, 1080x1920, audio claro)

## 📖 Recursos de Aprendizaje

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [MoviePy Documentation](https://zulko.github.io/moviepy/)
- [YouTube Shorts Best Practices](https://support.google.com/youtube/answer/10059070)

---

# 📤 Fase 4: YouTube Upload & Scheduler (1 semana)

## Objetivos de Aprendizaje

- Implementar OAuth 2.0 flow robusto para YouTube API
- Manejar quotas de YouTube API (crítico: solo 10,000 puntos/día)
- Scheduler inteligente para publicación automática
- Optimización de metadata para Shorts

## Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **OAuth 2.0 Refresh** | Tokens expiran cada hora | Auto-refresh con credentials storage |
| **YouTube API Quota** | Solo 10K puntos/día, upload=1600 | Quota tracking + prioritization |
| **Shorts Optimization** | Metadata específica para Shorts | Título, descripción, #Shorts, aspect ratio |
| **Scheduled Publishing** | Publicar en horarios óptimos | APScheduler + timezone-aware |

## Implementación Práctica

### Paso 1: YouTube Adapter con OAuth 2.0

```python
# src/redishort/adapters/youtube_adapter.py
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from pathlib import Path
import json
import structlog
from typing import Optional
from ..config.settings import settings

logger = structlog.get_logger()

class YouTubeQuotaExceeded(Exception):
    """
    Aprende: Custom exception para casos específicos
    - Permite manejar quota exceeded de forma diferente
    - Logging específico
    - Retry logic condicional
    """
    pass

class YouTubeAdapter:
    """
    Aprende: YouTube API con quota management
    - OAuth 2.0 con auto-refresh
    - Quota tracking (crítico: 1600 puntos por upload)
    - Resumable uploads (si falla a 80%, continúa desde ahí)
    - Shorts-specific metadata
    """

    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    UPLOAD_COST = 1600  # YouTube API quota cost per upload

    def __init__(self, credentials_file: Path, token_file: Path):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.youtube = self._get_authenticated_service()
        self.quota_used_today = self._load_quota_usage()
        self.logger = logger.bind(adapter="youtube")

    def _get_authenticated_service(self):
        """
        Aprende: OAuth 2.0 flow completo
        1. Intenta cargar token existente
        2. Si expiró, refresca automáticamente (¡CRÍTICO!)
        3. Si no existe, ejecuta OAuth flow (browser popup)
        4. Guarda token para futuros usos
        """
        creds = None

        # 1. Load existing token
        if self.token_file.exists():
            creds = Credentials.from_authorized_user_file(
                str(self.token_file),
                self.SCOPES
            )
            self.logger.info("loaded_existing_credentials")

        # 2. Refresh if expired
        if creds and creds.expired and creds.refresh_token:
            self.logger.info("refreshing_expired_credentials")
            try:
                creds.refresh(Request())
                self.logger.info("credentials_refreshed")
            except Exception as e:
                self.logger.error("credential_refresh_failed", error=str(e))
                # Si falla refresh, forzar nuevo OAuth flow
                creds = None

        # 3. New OAuth flow if no valid creds
        if not creds or not creds.valid:
            self.logger.info("starting_oauth_flow")

            if not self.credentials_file.exists():
                raise ValueError(
                    f"Client secrets file not found: {self.credentials_file}\n"
                    "Download from: https://console.cloud.google.com/apis/credentials"
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                str(self.credentials_file),
                self.SCOPES
            )

            # Run local server for OAuth callback
            creds = flow.run_local_server(
                port=0,
                success_message='Authorization successful! You can close this window.'
            )
            self.logger.info("oauth_flow_completed")

        # 4. Save credentials for next time
        self.token_file.write_text(creds.to_json())
        self.logger.info("credentials_saved", path=str(self.token_file))

        return build('youtube', 'v3', credentials=creds)

    def upload_video(
        self,
        video_path: Path,
        title: str,
        description: str,
        tags: list[str],
        privacy_status: str = "public"
    ) -> str:
        """
        Upload video to YouTube as Short

        Args:
            video_path: Path to video file (must be 9:16, <60sec)
            title: Video title (max 100 chars)
            description: Video description (include attribution!)
            tags: List of tags
            privacy_status: "public", "private", or "unlisted"

        Returns: YouTube video ID

        Aprende: Fail-fast con quota
        - Verifica quota ANTES de subir
        - Evita desperdiciar bandwidth y tiempo
        """
        # 1. Quota check
        daily_quota = settings.youtube_daily_quota
        if self.quota_used_today + self.UPLOAD_COST > daily_quota:
            raise YouTubeQuotaExceeded(
                f"Daily quota exceeded: {self.quota_used_today}/{daily_quota} used. "
                f"Upload costs {self.UPLOAD_COST} points."
            )

        # 2. Validate video file
        if not video_path.exists():
            raise ValueError(f"Video file not found: {video_path}")

        file_size_mb = video_path.stat().st_size / (1024 * 1024)
        self.logger.info("uploading_video", title=title, size_mb=f"{file_size_mb:.2f}")

        try:
            # 3. Prepare request body
            body = {
                'snippet': {
                    'title': title[:100],  # YouTube limit
                    'description': description,
                    'tags': tags + ['Shorts'],  # Always include 'Shorts' tag
                    'categoryId': '24'  # Entertainment category
                },
                'status': {
                    'privacyStatus': privacy_status,
                    'selfDeclaredMadeForKids': False,
                    # Aprende: No shorts-specific field needed, YouTube auto-detects by aspect ratio
                }
            }

            # 4. Create MediaFileUpload (resumable)
            media = MediaFileUpload(
                str(video_path),
                chunksize=1024*1024,  # 1MB chunks
                resumable=True,
                mimetype='video/mp4'
            )

            # 5. Execute upload
            request = self.youtube.videos().insert(
                part='snippet,status',
                body=body,
                media_body=media
            )

            self.logger.info("upload_started", title=title)
            response = self._execute_upload_with_retry(request)
            video_id = response['id']

            # 6. Track quota usage
            self.quota_used_today += self.UPLOAD_COST
            self._save_quota_usage()

            # 7. Get video URL
            video_url = f"https://youtube.com/shorts/{video_id}"

            self.logger.info(
                "video_uploaded",
                video_id=video_id,
                url=video_url,
                quota_used=self.quota_used_today,
                quota_remaining=daily_quota - self.quota_used_today
            )

            return video_id

        except HttpError as e:
            error_content = json.loads(e.content.decode('utf-8'))
            error_reason = error_content.get('error', {}).get('errors', [{}])[0].get('reason', 'unknown')

            self.logger.error(
                "upload_failed",
                status=e.resp.status,
                reason=error_reason,
                details=error_content
            )

            # Quota exceeded tiene mensaje específico
            if 'quotaExceeded' in error_reason:
                raise YouTubeQuotaExceeded(f"YouTube API quota exceeded: {error_content}")

            raise

        except Exception as e:
            self.logger.error("upload_failed_unexpected", error=str(e))
            raise

    def _execute_upload_with_retry(self, request):
        """
        Aprende: Resumable uploads con retry
        - Si falla en 80%, reintenta desde 80%
        - No re-sube todo el video
        - Max 3 retries con backoff
        """
        response = None
        error = None
        retry = 0
        max_retries = 3

        while response is None:
            try:
                status, response = request.next_chunk()

                if status:
                    progress_pct = int(status.progress() * 100)
                    self.logger.info("upload_progress", percent=progress_pct)

            except HttpError as e:
                if e.resp.status in [500, 502, 503, 504]:
                    # Server errors: retry
                    error = e
                    if retry < max_retries:
                        retry += 1
                        sleep_time = 2 ** retry
                        self.logger.warning(
                            "upload_retry",
                            attempt=retry,
                            max_retries=max_retries,
                            sleep_sec=sleep_time,
                            error=str(e)
                        )
                        import time
                        time.sleep(sleep_time)
                    else:
                        raise
                else:
                    # Client errors: don't retry
                    raise

        return response

    def _load_quota_usage(self) -> int:
        """
        Aprende: Persistent quota tracking
        - Guarda en archivo JSON con fecha
        - Reset automático a medianoche (UTC)
        """
        quota_file = Path("data/youtube_quota.json")
        quota_file.parent.mkdir(parents=True, exist_ok=True)

        if not quota_file.exists():
            return 0

        try:
            data = json.loads(quota_file.read_text())

            # Check if it's still today
            from datetime import datetime, timezone
            today = datetime.now(timezone.utc).date().isoformat()

            if data.get('date') == today:
                return data.get('quota_used', 0)
            else:
                # New day, reset
                return 0

        except Exception as e:
            self.logger.warning("quota_load_failed", error=str(e))
            return 0

    def _save_quota_usage(self):
        """Save current quota usage"""
        from datetime import datetime, timezone

        quota_file = Path("data/youtube_quota.json")
        quota_file.parent.mkdir(parents=True, exist_ok=True)

        data = {
            'date': datetime.now(timezone.utc).date().isoformat(),
            'quota_used': self.quota_used_today,
            'quota_limit': settings.youtube_daily_quota
        }

        quota_file.write_text(json.dumps(data, indent=2))

    def get_quota_status(self) -> dict:
        """
        Aprende: Quota status para monitoring
        - Cuánto has usado hoy
        - Cuántos videos más puedes subir
        - Cuándo se resetea
        """
        daily_quota = settings.youtube_daily_quota
        remaining = daily_quota - self.quota_used_today
        videos_remaining = remaining // self.UPLOAD_COST

        from datetime import datetime, timezone, timedelta
        now = datetime.now(timezone.utc)
        midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        hours_until_reset = (midnight - now).total_seconds() / 3600

        return {
            'quota_used': self.quota_used_today,
            'quota_limit': daily_quota,
            'quota_remaining': remaining,
            'videos_remaining': videos_remaining,
            'hours_until_reset': round(hours_until_reset, 1),
            'usage_percentage': (self.quota_used_today / daily_quota) * 100
        }
```

### Paso 2: Scheduler Inteligente

```python
# src/redishort/core/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timezone
import structlog
from typing import List
from ..domain.models import TweetLanguage, VideoStatus
from ..core.video_generation_service import VideoGenerationService
from ..adapters.youtube_adapter import YouTubeAdapter, YouTubeQuotaExceeded

logger = structlog.get_logger()

class IntelligentScheduler:
    """
    Aprende: Scheduler inteligente con priorización
    - Detecta tweets virales cada hora
    - Genera videos en batch
    - Sube en horarios óptimos (según audiencia)
    - Respeta quota de YouTube
    """

    def __init__(
        self,
        video_service: VideoGenerationService,
        youtube_adapter: YouTubeAdapter
    ):
        self.video_service = video_service
        self.youtube = youtube_adapter
        self.scheduler = AsyncIOScheduler(timezone='UTC')
        self.logger = logger.bind(component="scheduler")

    def setup_jobs(self):
        """
        Aprende: Cron patterns para diferentes tareas
        - Detección de viralidad: cada hora (contenido fresco)
        - Generación de videos: cada 2 horas
        - Upload: horarios específicos (engagement alto)
        """

        # Job 1: Detect viral tweets every hour
        self.scheduler.add_job(
            self._detect_viral_tweets_job,
            trigger=IntervalTrigger(hours=1),
            id="detect_viral_tweets",
            name="Detect viral tweets from X",
            max_instances=1,  # No overlapping runs
            coalesce=True  # Si se saltó una run, no ejecutar múltiples
        )

        # Job 2: Generate videos every 2 hours
        self.scheduler.add_job(
            self._generate_videos_job,
            trigger=IntervalTrigger(hours=2),
            id="generate_videos",
            name="Generate videos from viral tweets"
        )

        # Job 3: Upload videos at optimal times
        # Para audiencia hispanohablante: 12pm, 6pm, 9pm (hora España/México)
        optimal_hours = [12, 18, 21]  # UTC

        for hour in optimal_hours:
            self.scheduler.add_job(
                self._upload_videos_job,
                trigger=CronTrigger(hour=hour, minute=0),
                id=f"upload_videos_{hour}h",
                name=f"Upload videos at {hour}:00 UTC"
            )

        # Job 4: Daily quota reset notification (midnight UTC)
        self.scheduler.add_job(
            self._quota_reset_notification_job,
            trigger=CronTrigger(hour=0, minute=5),  # 00:05 UTC
            id="quota_reset_notification",
            name="YouTube quota reset notification"
        )

        self.logger.info("jobs_scheduled", count=len(self.scheduler.get_jobs()))

    async def _detect_viral_tweets_job(self):
        """
        Job: Detectar tweets virales

        Aprende: Job con error handling robusto
        - No debe fallar scheduler si job explota
        - Log detallado de errores
        - Continúa con siguiente job
        """
        try:
            self.logger.info("job_started", job="detect_viral_tweets")

            # Detectar tweets en español (prioritario)
            spanish_tweets = await self.video_service.virality_detector.detect_and_save_viral_tweets(
                language=TweetLanguage.SPANISH,
                limit=50
            )

            # También algunos en inglés como backup
            english_tweets = await self.video_service.virality_detector.detect_and_save_viral_tweets(
                language=TweetLanguage.ENGLISH,
                limit=20
            )

            total = len(spanish_tweets) + len(english_tweets)

            self.logger.info(
                "job_completed",
                job="detect_viral_tweets",
                spanish=len(spanish_tweets),
                english=len(english_tweets),
                total=total
            )

        except Exception as e:
            self.logger.error("job_failed", job="detect_viral_tweets", error=str(e))

    async def _generate_videos_job(self):
        """
        Job: Generar videos de tweets pendientes

        Aprende: Batch processing con límite
        - No genera todos de golpe (puede ser 100+)
        - Límite de 5 videos por run
        - Prioriza por virality score
        """
        try:
            self.logger.info("job_started", job="generate_videos")

            # Get top 5 unprocessed viral tweets
            tweets = self.video_service.tweet_repo.get_unprocessed_viral_tweets(
                min_virality_score=75,  # Solo los más virales
                language=TweetLanguage.SPANISH,  # Prioridad español
                limit=5
            )

            if not tweets:
                self.logger.info("no_tweets_to_process")
                return

            videos_generated = 0

            for tweet in tweets:
                try:
                    video = await self.video_service.generate_video_from_tweet(tweet.tweet_id)
                    videos_generated += 1

                    self.logger.info(
                        "video_generated_by_job",
                        tweet_id=tweet.tweet_id,
                        video_id=video.id
                    )

                except Exception as e:
                    self.logger.error(
                        "video_generation_failed_in_job",
                        tweet_id=tweet.tweet_id,
                        error=str(e)
                    )
                    # Continuar con siguiente tweet

            self.logger.info(
                "job_completed",
                job="generate_videos",
                processed=len(tweets),
                generated=videos_generated
            )

        except Exception as e:
            self.logger.error("job_failed", job="generate_videos", error=str(e))

    async def _upload_videos_job(self):
        """
        Job: Subir videos generados a YouTube

        Aprende: Upload con quota management
        - Verifica quota disponible
        - Sube hasta agotar quota o videos
        - Prioriza videos de tweets más virales
        """
        try:
            self.logger.info("job_started", job="upload_videos")

            # Check quota status
            quota_status = self.youtube.get_quota_status()

            if quota_status['videos_remaining'] <= 0:
                self.logger.warning(
                    "quota_exhausted",
                    quota_used=quota_status['quota_used'],
                    hours_until_reset=quota_status['hours_until_reset']
                )
                return

            # Get videos ready to upload
            videos = self.video_service.video_repo.get_by_status(VideoStatus.GENERATED)

            if not videos:
                self.logger.info("no_videos_to_upload")
                return

            # Limit by quota remaining
            max_videos = min(len(videos), quota_status['videos_remaining'])
            videos_to_upload = videos[:max_videos]

            self.logger.info(
                "upload_batch_starting",
                total_generated=len(videos),
                uploading=len(videos_to_upload),
                quota_remaining=quota_status['videos_remaining']
            )

            uploaded_count = 0

            for video in videos_to_upload:
                try:
                    # Update status
                    video.status = VideoStatus.UPLOADING
                    self.video_service.video_repo.save(video)

                    # Get tweet for metadata
                    tweet = self.video_service.tweet_repo.get_by_id(video.tweet_id)

                    # Upload to YouTube
                    youtube_id = self.youtube.upload_video(
                        video_path=Path(video.video_path),
                        title=video.title,
                        description=video.description,
                        tags=self._generate_tags(tweet),
                        privacy_status="public"
                    )

                    # Mark as uploaded
                    video.mark_as_uploaded(youtube_id)
                    self.video_service.video_repo.save(video)

                    uploaded_count += 1

                    self.logger.info(
                        "video_uploaded_by_job",
                        video_id=video.id,
                        youtube_id=youtube_id,
                        url=video.youtube_url
                    )

                except YouTubeQuotaExceeded as e:
                    self.logger.warning("quota_exceeded_during_upload", error=str(e))
                    # Detener uploads por hoy
                    break

                except Exception as e:
                    self.logger.error(
                        "upload_failed_in_job",
                        video_id=video.id,
                        error=str(e)
                    )
                    # Mark as failed
                    video.status = VideoStatus.FAILED
                    self.video_service.video_repo.save(video)
                    # Continuar con siguiente video

            self.logger.info(
                "job_completed",
                job="upload_videos",
                attempted=len(videos_to_upload),
                uploaded=uploaded_count,
                failed=len(videos_to_upload) - uploaded_count
            )

        except Exception as e:
            self.logger.error("job_failed", job="upload_videos", error=str(e))

    async def _quota_reset_notification_job(self):
        """
        Job: Notificación de reset de quota

        Aprende: Monitoring job
        - No hace trabajo pesado
        - Solo logging/notificaciones
        - Útil para debugging
        """
        quota_status = self.youtube.get_quota_status()

        self.logger.info(
            "youtube_quota_reset",
            previous_usage=quota_status['quota_used'],
            new_limit=quota_status['quota_limit']
        )

    def _generate_tags(self, tweet) -> List[str]:
        """
        Aprende: Tag generation para SEO
        - Mix de genéricos y específicos
        - Idioma del tweet
        - #Shorts siempre incluido
        """
        tags = ['Shorts', 'TwitterViral', 'ReaccionTweet']

        # Language-specific tags
        if tweet.language == TweetLanguage.SPANISH:
            tags.extend(['Español', 'Twitter', 'Viral', 'Polemico'])
        else:
            tags.extend(['English', 'Twitter', 'Trending'])

        # Author username (sin @)
        tags.append(tweet.author_username)

        return tags[:15]  # YouTube limit

    def start(self):
        """Start scheduler"""
        self.scheduler.start()
        self.logger.info("scheduler_started", jobs=len(self.scheduler.get_jobs()))

    def stop(self):
        """Stop scheduler"""
        self.scheduler.shutdown(wait=True)
        self.logger.info("scheduler_stopped")

    def get_job_status(self) -> dict:
        """
        Aprende: Status endpoint para monitoring
        - Cuándo se ejecutó último job
        - Próxima ejecución
        - Estado de cada job
        """
        jobs_status = []

        for job in self.scheduler.get_jobs():
            jobs_status.append({
                'id': job.id,
                'name': job.name,
                'next_run_time': job.next_run_time.isoformat() if job.next_run_time else None,
                'trigger': str(job.trigger)
            })

        return {
            'scheduler_running': self.scheduler.running,
            'jobs': jobs_status,
            'youtube_quota': self.youtube.get_quota_status()
        }
```

### Paso 3: CLI para Control Manual

```python
# src/redishort/cli.py
"""
Aprende: CLI para operaciones manuales
- Testing individual de componentes
- Override de scheduler (subir ahora, no esperar)
- Debugging
"""

import asyncio
import click
from pathlib import Path
from .config.settings import settings
from .observability.logging import logger

# Lazy imports para performance
def get_services():
    """Factory para services (lazy loading)"""
    # TODO: Implementar factory pattern
    pass

@click.group()
def cli():
    """Redishort CLI - Twitter Shorts Automation"""
    pass

@cli.command()
@click.option('--language', default='es', help='Language code (es, en)')
@click.option('--limit', default=50, help='Number of tweets to fetch')
def detect_viral(language, limit):
    """Detect and save viral tweets"""
    click.echo(f"🔍 Detecting viral tweets ({language})...")

    # TODO: Implementar
    click.echo(f"✅ Found {limit} viral tweets")

@cli.command()
@click.argument('tweet_id')
def generate_video(tweet_id):
    """Generate video from specific tweet ID"""
    click.echo(f"🎬 Generating video for tweet {tweet_id}...")

    # TODO: Implementar
    click.echo(f"✅ Video generated")

@cli.command()
def upload_pending():
    """Upload all pending videos to YouTube"""
    click.echo("📤 Uploading pending videos...")

    # Check quota first
    click.echo(f"YouTube Quota: X/10000 used")

    # TODO: Implementar
    click.echo("✅ Uploaded X videos")

@cli.command()
def quota_status():
    """Show YouTube API quota status"""
    # TODO: Implementar
    click.echo("YouTube Quota Status:")
    click.echo("  Used today: 3200/10000 (32%)")
    click.echo("  Videos remaining: 4")
    click.echo("  Resets in: 8.5 hours")

@cli.command()
def scheduler_start():
    """Start the scheduler daemon"""
    click.echo("🚀 Starting scheduler...")

    # TODO: Implementar
    click.echo("✅ Scheduler running. Press Ctrl+C to stop.")

@cli.command()
def scheduler_status():
    """Show scheduler status"""
    # TODO: Implementar
    click.echo("Scheduler Status:")
    click.echo("  Status: Running")
    click.echo("  Next jobs:")
    click.echo("    - detect_viral_tweets: in 15 minutes")
    click.echo("    - upload_videos: in 2 hours")

if __name__ == '__main__':
    cli()
```

### Paso 4: Testing de YouTube Upload

```python
# tests/integration/test_youtube_adapter.py
import pytest
from pathlib import Path
from redishort.adapters.youtube_adapter import YouTubeAdapter, YouTubeQuotaExceeded

@pytest.mark.integration
@pytest.mark.skipif(
    not Path("client_secrets.json").exists(),
    reason="YouTube credentials not available"
)
def test_youtube_oauth_flow():
    """
    Aprende: Test de OAuth flow
    - Solo corre si existen credenciales
    - Útil para validar setup inicial
    """
    adapter = YouTubeAdapter(
        credentials_file=Path("client_secrets.json"),
        token_file=Path("token.json")
    )

    # Should not raise
    assert adapter.youtube is not None

def test_quota_tracking():
    """Test quota tracking persistence"""
    adapter = YouTubeAdapter(...)

    initial_quota = adapter.quota_used_today

    # Simulate upload
    adapter.quota_used_today += adapter.UPLOAD_COST
    adapter._save_quota_usage()

    # Reload
    adapter2 = YouTubeAdapter(...)
    assert adapter2.quota_used_today == initial_quota + adapter.UPLOAD_COST

def test_quota_exceeded_before_upload():
    """Test que falla si quota está agotada"""
    adapter = YouTubeAdapter(...)
    adapter.quota_used_today = 9000  # Casi agotado

    with pytest.raises(YouTubeQuotaExceeded):
        adapter.upload_video(
            video_path=Path("test_video.mp4"),
            title="Test",
            description="Test",
            tags=[]
        )
```

## ✅ Criterios de Éxito (Fase 4)

- [ ] OAuth 2.0 flow funcionando (tokens se refrescan automáticamente)
- [ ] Quota tracking previene uploads cuando quota agotada
- [ ] Scheduler ejecuta jobs en horarios correctos
- [ ] CLI permite operaciones manuales
- [ ] Videos se suben correctamente como Shorts (YouTube los detecta)
- [ ] Logs estructurados de cada upload con YouTube video ID

## 📖 Recursos de Aprendizaje

- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [YouTube Shorts Upload Guide](https://support.google.com/youtube/answer/10059070)
- [OAuth 2.0 for TV and Limited Input Devices](https://developers.google.com/youtube/v3/guides/auth/devices)
- [APScheduler Documentation](https://apscheduler.readthedocs.io/)

---

# 🧪 Fase 5: Testing & CI/CD (1 semana)

## Objetivos de Aprendizaje

- Pirámide de testing (unit → integration → e2e)
- GitHub Actions para CI/CD
- Code coverage meaningful (>80%)
- Secrets management seguro

## Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **Test Pyramid** | Balance entre velocidad y confianza | 70% unit, 20% integration, 10% e2e |
| **Fixtures** | Reusabilidad de setup | pytest fixtures con scopes |
| **Mocking externo** | Tests rápidos sin APIs reales | Mock de X API, YouTube API |
| **Coverage meaningful** | No solo %, sino edge cases | Branch coverage, no solo line |

## Implementación Práctica

### Paso 1: Test Pyramid Completa

```python
# tests/conftest.py
"""
Aprende: pytest fixtures compartidas
- Scope session: Se crea una vez para todos los tests
- Scope function: Se crea/destruye por cada test
- Autouse: Se ejecuta automáticamente
"""

import pytest
from pathlib import Path
import tempfile
from redishort.config.settings import Settings
from redishort.domain.models import ViralTweet, TweetMetrics, TweetLanguage
from redishort.domain.repositories import TweetRepository, VideoRepository
from datetime import datetime, timedelta

@pytest.fixture(scope="session")
def test_assets_dir():
    """
    Aprende: Fixture con archivos reales de prueba
    - Videos de background cortos (2-3 sec)
    - Fuentes
    - Audio samples
    """
    assets_dir = Path(__file__).parent / "test_assets"
    if not assets_dir.exists():
        pytest.skip("Test assets not found")
    return assets_dir

@pytest.fixture
def temp_dir():
    """
    Aprende: Temporary directory que se limpia automáticamente
    - Cada test tiene su propio dir
    - Se borra después del test
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)

@pytest.fixture
def sample_viral_tweet():
    """Fixture: Tweet viral de ejemplo"""
    return ViralTweet(
        tweet_id="1234567890",
        author_username="test_user",
        author_display_name="Test User",
        text="Este es un tweet de prueba muy viral que generó mucha conversación y debate",
        created_at=datetime.utcnow() - timedelta(hours=2),
        metrics=TweetMetrics(
            likes=15000,
            retweets=3000,
            replies=800,
            views=500000
        ),
        language=TweetLanguage.SPANISH,
        url="https://twitter.com/test_user/status/1234567890",
        author_verified=True,
        author_followers=100000
    )

@pytest.fixture
def mock_twitter_api(monkeypatch):
    """
    Aprende: Monkey-patching para mock de APIs externas
    - Reemplaza llamadas reales con mocks
    - Tests no dependen de internet
    """
    def mock_fetch_trending_tweets(*args, **kwargs):
        # Retorna tweets fake
        return [
            ViralTweet(...),
            ViralTweet(...),
        ]

    monkeypatch.setattr(
        "redishort.adapters.twitter_api_strategy.TwitterAPIStrategy.fetch_trending_tweets",
        mock_fetch_trending_tweets
    )

class FakeTweetRepository(TweetRepository):
    """
    Aprende: Fake repository para tests
    - Más simple que mock
    - Comportamiento realista
    - Estado verificable
    """
    def __init__(self):
        self.tweets = {}
        self.processed = set()

    def save(self, tweet):
        self.tweets[tweet.tweet_id] = tweet

    def get_by_id(self, tweet_id):
        return self.tweets.get(tweet_id)

    def get_unprocessed_viral_tweets(self, min_virality_score=70, language=None, limit=10):
        unprocessed = [
            t for t in self.tweets.values()
            if t.tweet_id not in self.processed
            and t.calculate_virality_score().score >= min_virality_score
        ]
        if language:
            unprocessed = [t for t in unprocessed if t.language == language]
        return unprocessed[:limit]

    def mark_as_processed(self, tweet_id):
        self.processed.add(tweet_id)

    def get_recent_viral_tweets(self, hours=24, language=None):
        # Implementación simplificada
        return list(self.tweets.values())

@pytest.fixture
def fake_tweet_repo():
    return FakeTweetRepository()
```

### Paso 2: Unit Tests Exhaustivos

```python
# tests/unit/test_virality_algorithm.py
"""
Aprende: Tests del algoritmo de viralidad
- Múltiples escenarios (happy path + edge cases)
- Assertions específicas
- Datos variados para cubrir rangos
"""

import pytest
from datetime import datetime, timedelta
from redishort.domain.models import ViralTweet, TweetMetrics, TweetLanguage

class TestViralityAlgorithm:
    """
    Aprende: Test class para agrupar tests relacionados
    - Nomenclatura: test_<scenario>_<expected_behavior>
    """

    def test_recent_high_engagement_is_viral(self):
        """Tweet reciente + alto engagement = VIRAL"""
        tweet = ViralTweet(
            tweet_id="1",
            author_username="user",
            author_display_name="User",
            text="Tweet viral test",
            created_at=datetime.utcnow() - timedelta(hours=1),  # Muy reciente
            metrics=TweetMetrics(likes=20000, retweets=4000, replies=1000),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/1"
        )

        score = tweet.calculate_virality_score()

        assert score.is_viral
        assert score.score > 80  # Score muy alto
        assert score.recency_score > 95  # Muy reciente
        assert score.language_bonus == 20  # Español

    def test_old_tweet_not_viral(self):
        """Tweet antiguo (>48h) NO es viral, incluso con engagement"""
        tweet = ViralTweet(
            tweet_id="2",
            author_username="user",
            author_display_name="User",
            text="Tweet antiguo",
            created_at=datetime.utcnow() - timedelta(hours=72),  # 3 días
            metrics=TweetMetrics(likes=10000, retweets=2000, replies=500),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/2"
        )

        score = tweet.calculate_virality_score()

        assert not score.is_viral
        assert score.recency_score < 20  # Muy bajo

    def test_low_engagement_not_viral(self):
        """Tweet con poco engagement NO es viral"""
        tweet = ViralTweet(
            tweet_id="3",
            author_username="user",
            author_display_name="User",
            text="Tweet sin engagement",
            created_at=datetime.utcnow() - timedelta(minutes=30),
            metrics=TweetMetrics(likes=10, retweets=2, replies=1),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/3"
        )

        score = tweet.calculate_virality_score()

        assert not score.is_viral
        assert score.engagement_score < 30

    def test_velocity_score_importance(self):
        """
        Aprende: Test de velocity (engagement/hora)
        - Tweet con 10K likes en 1 hora > tweet con 10K likes en 24 horas
        """
        # Tweet rápido (1 hora)
        fast_tweet = ViralTweet(
            tweet_id="4",
            author_username="user",
            author_display_name="User",
            text="Tweet rápido",
            created_at=datetime.utcnow() - timedelta(hours=1),
            metrics=TweetMetrics(likes=10000, retweets=2000, replies=500),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/4"
        )

        # Tweet lento (24 horas)
        slow_tweet = ViralTweet(
            tweet_id="5",
            author_username="user",
            author_display_name="User",
            text="Tweet lento",
            created_at=datetime.utcnow() - timedelta(hours=24),
            metrics=TweetMetrics(likes=10000, retweets=2000, replies=500),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/5"
        )

        fast_score = fast_tweet.calculate_virality_score()
        slow_score = slow_tweet.calculate_virality_score()

        # Tweet rápido debe tener velocity score mucho mayor
        assert fast_score.velocity_score > slow_score.velocity_score * 2

    def test_language_bonus_applied(self):
        """Test que español tiene +20 puntos de bonus"""
        spanish_tweet = ViralTweet(
            tweet_id="6",
            author_username="user",
            author_display_name="User",
            text="Tweet en español",
            created_at=datetime.utcnow() - timedelta(hours=2),
            metrics=TweetMetrics(likes=5000, retweets=1000, replies=200),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/6"
        )

        english_tweet = ViralTweet(
            tweet_id="7",
            author_username="user",
            author_display_name="User",
            text="Tweet in English",
            created_at=datetime.utcnow() - timedelta(hours=2),
            metrics=TweetMetrics(likes=5000, retweets=1000, replies=200),
            language=TweetLanguage.ENGLISH,
            url="https://twitter.com/user/status/7"
        )

        spanish_score = spanish_tweet.calculate_virality_score()
        english_score = english_tweet.calculate_virality_score()

        assert spanish_score.language_bonus == 20
        assert english_score.language_bonus == 0
        assert spanish_score.score > english_score.score

    @pytest.mark.parametrize("likes,retweets,replies,expected_viral", [
        (100, 10, 5, False),          # Bajo engagement
        (1000, 200, 50, False),       # Medio-bajo
        (5000, 1000, 300, True),      # Medio-alto
        (20000, 5000, 1500, True),    # Alto
        (100000, 20000, 5000, True),  # Ultra viral
    ])
    def test_engagement_thresholds(self, likes, retweets, replies, expected_viral):
        """
        Aprende: Parametrized tests
        - Múltiples casos con misma lógica
        - Tabla de datos de entrada/salida esperada
        """
        tweet = ViralTweet(
            tweet_id="test",
            author_username="user",
            author_display_name="User",
            text="Test tweet",
            created_at=datetime.utcnow() - timedelta(hours=2),
            metrics=TweetMetrics(likes=likes, retweets=retweets, replies=replies),
            language=TweetLanguage.SPANISH,
            url="https://twitter.com/user/status/test"
        )

        score = tweet.calculate_virality_score()
        assert score.is_viral == expected_viral
```

### Paso 3: Integration Tests

```python
# tests/integration/test_video_generation_pipeline.py
"""
Aprende: Integration tests
- Tocan múltiples componentes
- Usan filesystem real
- Más lentos pero más realistas
"""

import pytest
import asyncio
from pathlib import Path
from redishort.core.video_generation_service import VideoGenerationService
from redishort.video.tweet_visualizer import TweetVisualizer
from redishort.video.video_composer import VideoComposer

@pytest.mark.integration
@pytest.mark.slow
async def test_full_video_generation_pipeline(
    sample_viral_tweet,
    fake_tweet_repo,
    temp_dir,
    test_assets_dir
):
    """
    Aprende: Test end-to-end del pipeline de video
    - Genera video real de tweet
    - Verifica que archivo existe y tiene tamaño razonable
    - Lento (~30-60 segundos)
    """
    # Setup
    fake_tweet_repo.save(sample_viral_tweet)

    visualizer = TweetVisualizer(
        assets_dir=test_assets_dir,
        output_dir=temp_dir / "images"
    )

    composer = VideoComposer(
        assets_dir=test_assets_dir,
        output_dir=temp_dir / "videos"
    )

    # Mock adapters (TTS, Gemini) para test rápido
    # En producción, estos harían llamadas reales

    service = VideoGenerationService(
        tweet_repo=fake_tweet_repo,
        video_repo=FakeVideoRepository(),
        script_generator=MockScriptGenerator(),
        tts_adapter=MockTTSAdapter(temp_dir / "audio"),
        tweet_visualizer=visualizer,
        video_composer=composer
    )

    # Execute
    video = await service.generate_video_from_tweet(sample_viral_tweet.tweet_id)

    # Assert
    assert video.status == VideoStatus.GENERATED
    assert Path(video.video_path).exists()

    # Check file size (should be >100KB for real video)
    file_size = Path(video.video_path).stat().st_size
    assert file_size > 100 * 1024  # >100KB

    # Check video metadata (optional, requires moviepy)
    # from moviepy.editor import VideoFileClip
    # clip = VideoFileClip(video.video_path)
    # assert clip.duration > 10  # At least 10 seconds
    # assert clip.size == (1080, 1920)  # 9:16 aspect ratio
```

### Paso 4: GitHub Actions CI/CD

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        echo "$HOME/.local/bin" >> $GITHUB_PATH

    - name: Install dependencies
      run: |
        poetry install --no-interaction

    - name: Run linter (ruff)
      run: |
        poetry run ruff check src/ tests/

    - name: Run type checker (mypy)
      run: |
        poetry run mypy src/
      continue-on-error: true  # No fallar por type hints (por ahora)

    - name: Run unit tests
      run: |
        poetry run pytest tests/unit -v \
          --cov=src \
          --cov-report=xml \
          --cov-report=term-missing \
          --durations=10

    - name: Run integration tests
      run: |
        poetry run pytest tests/integration -v -m integration
      env:
        # Test credentials (no funcionales, solo para testing)
        TWITTER_SOURCE_MODE: scraping
        GOOGLE_API_KEY: ${{ secrets.TEST_GOOGLE_API_KEY }}

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v4
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella

    - name: Check coverage threshold
      run: |
        poetry run pytest --cov=src --cov-fail-under=80

  security:
    name: Security Scan
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Run Bandit (security linter)
      run: |
        pip install bandit
        bandit -r src/ -f json -o bandit-report.json
      continue-on-error: true

    - name: Upload Bandit report
      uses: actions/upload-artifact@v4
      with:
        name: bandit-report
        path: bandit-report.json

  build-docker:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: test

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Build Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        file: ./docker/Dockerfile.prod
        push: false
        tags: redishort:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

    - name: Test Docker image
      run: |
        docker run redishort:${{ github.sha }} poetry run pytest tests/unit -v

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: [test, build-docker]
    if: github.ref == 'refs/heads/develop'

    steps:
    - name: Deploy to staging
      run: |
        echo "🚀 Deploying to staging environment..."
        # TODO: Implementar deployment real (Docker Compose, Kubernetes, etc.)

  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: [test, build-docker]
    if: github.ref == 'refs/heads/main'

    steps:
    - name: Deploy to production
      run: |
        echo "🚀 Deploying to production environment..."
        # TODO: Implementar deployment real
```

### Paso 5: Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
"""
Aprende: Pre-commit hooks
- Se ejecutan antes de cada commit
- Previenen commits con errores obvios
- Formatean código automáticamente
"""

repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.13
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=10000']
      - id: check-json
      - id: check-toml
      - id: detect-private-key

  - repo: local
    hooks:
      - id: pytest-unit
        name: pytest-unit
        entry: poetry run pytest tests/unit -v --tb=short
        language: system
        pass_filenames: false
        always_run: true
```

## ✅ Criterios de Éxito (Fase 5)

- [ ] >80% code coverage (unit tests)
- [ ] CI passing en GitHub Actions
- [ ] Pre-commit hooks instalados y funcionando
- [ ] Integration tests cubren pipeline completo
- [ ] Security scan sin vulnerabilidades críticas
- [ ] Docker image se construye sin errores

## 📖 Recursos de Aprendizaje

- [pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Codecov Documentation](https://docs.codecov.com/)

---

# 🚀 Fase 6: Production-Ready & Observability (1 semana)

## Objetivos de Aprendizaje

- Observability completa (logs, metrics, traces)
- Docker deployment production-ready
- Alerting cuando algo falla
- Cost optimization

## Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **Prometheus Metrics** | Monitoreo de performance | Videos generados/hora, virality scores, etc |
| **Grafana Dashboards** | Visualización de métricas | Dashboard personalizado |
| **Alerting** | Notificaciones de problemas | Alert cuando quota se agota, fallos, etc |
| **Structured Logging** | Debugging en producción | JSON logs parseables |

## Implementación Práctica

### Paso 1: Prometheus Metrics

```python
# src/redishort/observability/metrics.py
"""
Aprende: Prometheus metrics para observability
- Counter: Contador que solo sube (requests, errors)
- Gauge: Valor que sube/baja (queue size, quota usage)
- Histogram: Distribución de valores (latency, video duration)
"""

from prometheus_client import (
    Counter, Gauge, Histogram, Info,
    start_http_server, generate_latest
)
import structlog

logger = structlog.get_logger()

# === Counters (solo suben) ===

tweets_fetched_total = Counter(
    'tweets_fetched_total',
    'Total tweets fetched from X',
    ['language', 'source']  # Labels para filtrar
)

videos_generated_total = Counter(
    'videos_generated_total',
    'Total videos generated',
    ['status']  # success, failed
)

videos_uploaded_total = Counter(
    'videos_uploaded_total',
    'Total videos uploaded to YouTube',
    ['status']
)

api_requests_total = Counter(
    'api_requests_total',
    'Total API requests',
    ['api', 'endpoint', 'status_code']
)

# === Gauges (suben y bajan) ===

youtube_quota_used = Gauge(
    'youtube_quota_used',
    'YouTube API quota used today'
)

youtube_quota_remaining = Gauge(
    'youtube_quota_remaining',
    'YouTube API quota remaining today'
)

pending_videos = Gauge(
    'pending_videos',
    'Number of videos pending upload'
)

processing_videos = Gauge(
    'processing_videos',
    'Number of videos currently being processed'
)

# === Histograms (distribuciones) ===

video_generation_duration_seconds = Histogram(
    'video_generation_duration_seconds',
    'Time to generate video (seconds)',
    buckets=[10, 30, 60, 120, 300, 600]  # 10s, 30s, 1min, 2min, 5min, 10min
)

video_duration_seconds = Histogram(
    'video_duration_seconds',
    'Duration of generated videos (seconds)',
    buckets=[5, 10, 15, 20, 30, 45, 60]
)

virality_score_distribution = Histogram(
    'virality_score_distribution',
    'Distribution of virality scores',
    buckets=[0, 50, 60, 70, 75, 80, 85, 90, 95, 100]
)

tweet_engagement_total = Histogram(
    'tweet_engagement_total',
    'Total engagement (likes + RT*2 + replies*3)',
    buckets=[100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
)

# === Info (metadata estática) ===

app_info = Info('app_info', 'Application information')
app_info.info({
    'version': '2.0.0',
    'environment': 'production',
    'twitter_source_mode': 'api_official'
})

def start_metrics_server(port: int = 9090):
    """
    Aprende: Exponer métricas en /metrics endpoint
    - Prometheus scrapea este endpoint cada X segundos
    - No bloquea la app (servidor HTTP separado)
    """
    start_http_server(port)
    logger.info("metrics_server_started", port=port, endpoint=f"http://localhost:{port}/metrics")

# === Helper decorators ===

def track_video_generation(func):
    """
    Aprende: Decorator para tracking automático
    - Mide duración
    - Cuenta éxitos/fallos
    - Actualiza gauges
    """
    async def wrapper(*args, **kwargs):
        processing_videos.inc()

        with video_generation_duration_seconds.time():
            try:
                result = await func(*args, **kwargs)
                videos_generated_total.labels(status='success').inc()
                return result
            except Exception as e:
                videos_generated_total.labels(status='failed').inc()
                raise
            finally:
                processing_videos.dec()

    return wrapper
```

### Paso 2: Grafana Dashboard (JSON config)

```json
{
  "dashboard": {
    "title": "Redishort - Twitter Shorts Automation",
    "panels": [
      {
        "title": "Videos Generated (24h)",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(increase(videos_generated_total{status=\"success\"}[24h]))"
          }
        ]
      },
      {
        "title": "YouTube Quota Usage",
        "type": "gauge",
        "targets": [
          {
            "expr": "youtube_quota_used / 10000 * 100"
          }
        ],
        "fieldConfig": {
          "max": 100,
          "thresholds": [
            {"color": "green", "value": 0},
            {"color": "yellow", "value": 70},
            {"color": "red", "value": 90}
          ]
        }
      },
      {
        "title": "Video Generation Duration (p95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(video_generation_duration_seconds_bucket[5m]))"
          }
        ]
      },
      {
        "title": "Virality Score Distribution",
        "type": "heatmap",
        "targets": [
          {
            "expr": "rate(virality_score_distribution_bucket[5m])"
          }
        ]
      },
      {
        "title": "API Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(api_requests_total[5m])",
            "legendFormat": "{{api}} - {{endpoint}}"
          }
        ]
      },
      {
        "title": "Pending Videos",
        "type": "stat",
        "targets": [
          {
            "expr": "pending_videos"
          }
        ]
      }
    ]
  }
}
```

### Paso 3: Alerting con Prometheus Alertmanager

```yaml
# prometheus/alerts.yml
"""
Aprende: Alertas para eventos críticos
- Se envían a Slack, email, PagerDuty, etc
- Configurables por severidad
"""

groups:
  - name: redishort_alerts
    interval: 1m
    rules:
      # Alert: YouTube quota casi agotada
      - alert: YouTubeQuotaNearlyExhausted
        expr: youtube_quota_used / 10000 > 0.9
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "YouTube API quota nearly exhausted"
          description: "YouTube quota is at {{ $value | humanizePercentage }}. Remaining: {{ query \"youtube_quota_remaining\" }} points."

      # Alert: No videos generated en 6 horas
      - alert: NoVideosGenerated
        expr: increase(videos_generated_total{status="success"}[6h]) == 0
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "No videos generated in the last 6 hours"
          description: "The video generation pipeline may be stuck or failing."

      # Alert: Alto rate de fallos
      - alert: HighVideoGenerationFailureRate
        expr: |
          rate(videos_generated_total{status="failed"}[1h]) /
          rate(videos_generated_total[1h]) > 0.5
        for: 15m
        labels:
          severity: critical
        annotations:
          summary: "High video generation failure rate"
          description: "More than 50% of video generations are failing."

      # Alert: API errors spike
      - alert: APIErrorSpike
        expr: |
          rate(api_requests_total{status_code=~"5.."}[5m]) > 0.1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "API error rate spike detected"
          description: "API {{$labels.api}} is returning 5xx errors at {{ $value }} req/s."

      # Alert: Video generation muy lenta
      - alert: SlowVideoGeneration
        expr: |
          histogram_quantile(0.95,
            rate(video_generation_duration_seconds_bucket[10m])
          ) > 300
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Video generation is slow"
          description: "95th percentile of video generation time is {{ $value }}s (threshold: 300s)."
```

### Paso 4: Production Dockerfile (Multi-stage)

```dockerfile
# docker/Dockerfile.prod
"""
Aprende: Multi-stage build
- Stage 1: Builder (instala deps, compila)
- Stage 2: Runtime (solo lo necesario para correr)
- Resultado: Imagen pequeña (~500MB vs ~2GB)
"""

# ============= Stage 1: Builder =============
FROM python:3.11-slim as builder

WORKDIR /build

# Install Poetry
RUN pip install poetry==1.7.1

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
# --no-dev: Sin dependencias de desarrollo
# --no-root: Sin instalar el paquete aún
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-root --no-interaction --no-ansi

# Copy application code
COPY src/ ./src/

# Install the package
RUN poetry install --no-dev --no-interaction --no-ansi


# ============= Stage 2: Runtime =============
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (ffmpeg para video processing)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /build/.venv /app/.venv

# Copy application code
COPY src/ ./src/
COPY assets/ ./assets/

# Create non-root user (security best practice)
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app && \
    mkdir -p /app/data /app/output && \
    chown -R appuser:appuser /app/data /app/output

USER appuser

# Environment
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expose metrics port
EXPOSE 9090

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:9090/metrics')" || exit 1

# Run application
CMD ["python", "-m", "redishort.main"]
```

### Paso 5: Docker Compose para Producción

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: docker/Dockerfile.prod
    container_name: redishort-app
    restart: unless-stopped
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
    env_file:
      - .env.production
    volumes:
      - ./data:/app/data
      - ./output:/app/output
      - ./logs:/app/logs
    ports:
      - "9090:9090"  # Metrics
    depends_on:
      - postgres
      - redis
    networks:
      - redishort-network

  postgres:
    image: postgres:15-alpine
    container_name: redishort-db
    restart: unless-stopped
    environment:
      POSTGRES_DB: redishort
      POSTGRES_USER: redishort
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - redishort-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U redishort"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: redishort-redis
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - redishort-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  prometheus:
    image: prom/prometheus:latest
    container_name: redishort-prometheus
    restart: unless-stopped
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/usr/share/prometheus/console_libraries'
      - '--web.console.templates=/usr/share/prometheus/consoles'
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./prometheus/alerts.yml:/etc/prometheus/alerts.yml
      - prometheus_data:/prometheus
    ports:
      - "9091:9090"
    networks:
      - redishort-network

  grafana:
    image: grafana/grafana:latest
    container_name: redishort-grafana
    restart: unless-stopped
    environment:
      - GF_SECURITY_ADMIN_PASSWORD__FILE=/run/secrets/grafana_password
      - GF_USERS_ALLOW_SIGN_UP=false
    secrets:
      - grafana_password
    volumes:
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./grafana/datasources:/etc/grafana/provisioning/datasources
      - grafana_data:/var/lib/grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
    networks:
      - redishort-network

  alertmanager:
    image: prom/alertmanager:latest
    container_name: redishort-alertmanager
    restart: unless-stopped
    command:
      - '--config.file=/etc/alertmanager/alertmanager.yml'
      - '--storage.path=/alertmanager'
    volumes:
      - ./prometheus/alertmanager.yml:/etc/alertmanager/alertmanager.yml
      - alertmanager_data:/alertmanager
    ports:
      - "9093:9093"
    networks:
      - redishort-network

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
  alertmanager_data:

networks:
  redishort-network:
    driver: bridge

secrets:
  db_password:
    file: ./secrets/db_password.txt
  grafana_password:
    file: ./secrets/grafana_password.txt
```

### Paso 6: Deployment Script

```bash
# scripts/deploy.sh
#!/bin/bash
set -e

echo "🚀 Deploying Redishort to Production..."

# 1. Pull latest code
echo "📥 Pulling latest code..."
git pull origin main

# 2. Build Docker images
echo "🐳 Building Docker images..."
docker-compose -f docker-compose.prod.yml build --no-cache

# 3. Run database migrations (if any)
echo "🗄️ Running database migrations..."
# TODO: Implement migrations

# 4. Stop old containers
echo "🛑 Stopping old containers..."
docker-compose -f docker-compose.prod.yml down

# 5. Start new containers
echo "▶️ Starting new containers..."
docker-compose -f docker-compose.prod.yml up -d

# 6. Wait for services to be healthy
echo "⏳ Waiting for services to be healthy..."
sleep 10

# 7. Check health
echo "🏥 Checking service health..."
docker-compose -f docker-compose.prod.yml ps

# 8. Verify metrics endpoint
echo "📊 Verifying metrics endpoint..."
curl -f http://localhost:9090/metrics || echo "⚠️ Metrics endpoint not responding"

echo "✅ Deployment complete!"
echo "📊 Grafana: http://localhost:3000"
echo "📈 Prometheus: http://localhost:9091"
```

## ✅ Criterios de Éxito (Fase 6)

- [ ] Prometheus metrics expuestos en /metrics
- [ ] Grafana dashboard funcionando con visualizaciones
- [ ] Alertas configuradas y probadas
- [ ] Docker compose up funciona end-to-end
- [ ] Health checks pasando
- [ ] Logs estructurados (JSON) en producción
- [ ] Deployment script automatizado

## 📖 Recursos de Aprendizaje

- [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [Grafana Tutorials](https://grafana.com/tutorials/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [The Twelve-Factor App](https://12factor.net/)

---

# 📊 Resumen del Roadmap Completo

## Duración Total: 9-10 semanas

| Fase | Duración | Enfoque | Tecnologías Clave | Entregables |
|------|----------|---------|-------------------|-------------|
| **Fase 0** | 1 semana | Setup & Tooling | Poetry, Pydantic, structlog | Settings, logging, .env |
| **Fase 1** | 2 semanas | Core Architecture | DDD, SOLID, Repository pattern | Domain models, tests |
| **Fase 2** | 2 semanas | Twitter Adapters | Strategy pattern, retry, circuit breaker | TwitterAdapter, viralidad |
| **Fase 3** | 2 semanas | Video Pipeline | Pillow, MoviePy, Gemini, async | TweetVisualizer, Composer |
| **Fase 4** | 1 semana | YouTube & Scheduler | OAuth 2.0, APScheduler | YouTubeAdapter, CLI |
| **Fase 5** | 1 semana | Testing & CI/CD | pytest, GitHub Actions, coverage | Tests, CI pipeline |
| **Fase 6** | 1 semana | Production | Prometheus, Grafana, Docker | Metrics, dashboards, deploy |

## 🎯 Conceptos Dominados

Al completar este roadmap, habrás dominado:

### Arquitectura
- ✅ Clean Architecture / Hexagonal Architecture
- ✅ Domain-Driven Design (Value Objects, Entities, Services)
- ✅ SOLID principles en práctica
- ✅ Dependency Injection
- ✅ Repository & Strategy patterns

### Resiliencia
- ✅ Retry with exponential backoff
- ✅ Circuit breaker
- ✅ Rate limiting (critical para X API)
- ✅ Graceful degradation
- ✅ Quota management

### Testing
- ✅ Test pyramid (unit > integration > e2e)
- ✅ Fakes > Mocks
- ✅ Parametrized tests
- ✅ >80% meaningful coverage

### DevOps
- ✅ Docker multi-stage builds
- ✅ CI/CD con GitHub Actions
- ✅ Secrets management seguro
- ✅ Health checks
- ✅ Automated deployment

### Observability
- ✅ Structured logging (JSON)
- ✅ Prometheus metrics
- ✅ Grafana dashboards
- ✅ Alertmanager
- ✅ Distributed tracing (opcional)

### Domain-Specific
- ✅ OAuth 2.0 flow completo
- ✅ API rate limiting (X y YouTube)
- ✅ Virality scoring algorithm
- ✅ Content moderation
- ✅ Multimedia processing (video, audio, images)
- ✅ Prompt engineering (Gemini)

---

# 🔧 Apéndice A: Troubleshooting Común

## Problema 1: X API Rate Limiting

**Síntoma**: `429 Too Many Requests` de X API

**Diagnóstico**:
```bash
# Ver logs de rate limiting
docker logs redishort-app | grep "rate_limit"
```

**Solución**:
1. Verifica que `@limits` decorator está aplicado
2. Reduce frecuencia de fetching (cada 2h en lugar de 1h)
3. Considera cambiar a tier superior de API

```python
# Ajustar rate limit en settings
TWITTER_API_RATE_LIMIT_CALLS=30  # Reduce de 50 a 30
```

## Problema 2: YouTube Quota Agotada

**Síntoma**: `YouTubeQuotaExceeded` exception

**Diagnóstico**:
```bash
curl http://localhost:9090/metrics | grep youtube_quota
```

**Solución**:
1. Esperar a reset (medianoche UTC)
2. Reducir número de uploads por día
3. Priorizar solo tweets ultra-virales (score >85)

```python
# Ajustar threshold de viralidad
VIRALITY_MIN_SCORE=85  # Más estricto
```

## Problema 3: Video Generation Memory Leak

**Síntoma**: Container usa cada vez más memoria hasta crash

**Diagnóstico**:
```bash
docker stats redishort-app
```

**Solución**:
1. Verifica que todos los clips de MoviePy se cierran
2. Usa context managers (`with managed_clip(...)`)
3. Limita videos en paralelo

```python
# Forzar garbage collection después de cada video
import gc
gc.collect()
```

## Problema 4: Gemini API Bloqueado

**Síntoma**: `BlockedPromptException` o `StopCandidateException`

**Diagnóstico**:
```bash
# Ver qué tweets están siendo bloqueados
docker logs redishort-app | grep "prompt_blocked"
```

**Solución**:
1. Mejora content moderator (más keywords)
2. Ajusta safety settings de Gemini
3. Implementa retry con prompt alternativo

---

# 🚀 Apéndice B: Optimizaciones Avanzadas

## Optimización 1: Caching de Tweets

```python
# src/redishort/adapters/cached_twitter_adapter.py
from functools import lru_cache
from datetime import datetime, timedelta

class CachedTwitterAdapter:
    """
    Aprende: Caching para reducir API calls
    - Cache de 15 minutos para trending tweets
    - Reduce costos y rate limiting
    """

    @lru_cache(maxsize=100)
    def fetch_viral_tweets_cached(self, language, limit, cache_key):
        return self.strategy.fetch_trending_tweets(language, limit)

    def fetch_viral_tweets(self, language, limit):
        # Cache key con timestamp redondeado a 15 min
        now = datetime.utcnow()
        cache_timestamp = now.replace(minute=(now.minute // 15) * 15, second=0)
        cache_key = f"{language}_{limit}_{cache_timestamp.isoformat()}"

        return self.fetch_viral_tweets_cached(language, limit, cache_key)
```

## Optimización 2: Batch Video Generation

```python
# Generar múltiples videos en paralelo
async def generate_videos_batch(tweet_ids: list[str]) -> list[GeneratedVideo]:
    """
    Aprende: Paralelización con asyncio
    - Genera 5 videos a la vez
    - 5x más rápido que secuencial
    """
    tasks = [
        video_service.generate_video_from_tweet(tid)
        for tid in tweet_ids
    ]

    return await asyncio.gather(*tasks, return_exceptions=True)
```

## Optimización 3: Video Template System

```python
# Pre-render templates de tweets
class TweetTemplateCache:
    """
    Aprende: Pre-generación de templates
    - Genera layouts comunes al inicio
    - Reutiliza backgrounds
    - 2-3x más rápido
    """

    def __init__(self):
        self.templates = {}
        self._pregenerate_templates()

    def _pregenerate_templates(self):
        # Generar templates para diferentes tamaños de texto
        for char_count in [50, 100, 150, 200, 280]:
            template = self._generate_template(char_count)
            self.templates[char_count] = template
```

---

# 💰 Apéndice C: Métricas de Éxito del Negocio

## KPIs a Monitorear

### Métricas de Contenido

| Métrica | Target | Cómo Medir |
|---------|--------|------------|
| **Videos publicados/día** | 5-10 | YouTube API + logs |
| **Tasa de viralidad** | >70% tweets usados son virales | `virality_score > 70` |
| **Tiempo de generación** | <2 min por video | Prometheus histogram |
| **Tasa de éxito** | >95% videos generados correctamente | `videos_generated_total{status="success"}` |

### Métricas de YouTube

| Métrica | Target (primer mes) | Cómo Medir |
|---------|---------------------|------------|
| **Views** | 10K-50K | YouTube Analytics API |
| **Engagement rate** | >5% | (likes + comments) / views |
| **CTR** | >8% | YouTube Analytics |
| **Watch time promedio** | >60% del video | YouTube Analytics |
| **Subscribers growth** | +100/semana | YouTube Analytics |

### Métricas de Costos

| Concepto | Costo Mensual | Optimización |
|----------|---------------|--------------|
| **X API (Basic)** | $100 | Cachar requests, usar scraping como fallback |
| **Gemini API** | $20-50 | 1M tokens gratis, luego $0.0025/1K |
| **Google Cloud TTS** | $50-100 | Cachar audio común ("¿Tú qué opinas?") |
| **Hosting (VPS)** | $20-50 | DigitalOcean, Hetzner, AWS Lightsail |
| **TOTAL** | **$190-300/mes** | Break-even con AdSense: ~200K views/mes |

---

# 📈 Apéndice D: Estrategia de Monetización

## Fase 1: Validación (Mes 1-2)

**Objetivo**: Validar que el contenido funciona

- [ ] Publicar 5-10 videos/día consistentemente
- [ ] Alcanzar 1,000 subscribers (requisito YouTube Partner)
- [ ] Conseguir 4,000 horas de watch time (requisito monetización)
- [ ] CTR >8%, engagement >5%

**Métricas clave**:
- Views/video: >1,000
- Retention promedio: >50%
- Growth rate: +10% suscriptores/semana

## Fase 2: Monetización (Mes 3-6)

**YouTube Partner Program**:
- RPM (Revenue per Mille): $1-5 USD/1000 views (español)
- 200K views/mes = $200-1000 USD/mes
- Break-even: ~200K views/mes

**Optimizaciones para RPM**:
- Videos >8 segundos (requisito monetización Shorts)
- Evitar contenido controversial (amarillo en demonetización)
- Máximo engagement (likes, comments, shares)

## Fase 3: Escalabilidad (Mes 6+)

**Múltiples canales**:
- Canal principal: General (humor, polémicas)
- Canal 2: Fútbol/deportes
- Canal 3: Tech Twitter
- Canal 4: Drama de famosos

**Diversificación de ingresos**:
- AdSense: Base ($500-2000/mes por canal)
- Sponsorships: $50-500 por video sponsored
- Affiliate links: Amazon, servicios
- Merchandise: Si alcanzas 50K+ subs

---

# 🗺️ Apéndice E: Roadmap Post-MVP

## Fase 7: Features Avanzados (opcional)

### 7.1 Multi-Language Support
- Detectar idioma del tweet automáticamente
- TTS en múltiples idiomas
- Traducción automática de tweets

### 7.2 AI-Powered Thumbnail Generation
- Generar thumbnails atractivos con DALL-E/Midjourney
- A/B testing de thumbnails

### 7.3 Trending Topics Auto-Detection
- ML model para predecir qué tweets se volverán virales
- Publicar antes que la competencia

### 7.4 Interactive Elements
- Polls en Shorts
- Stickers animados
- Effects con OpenCV

### 7.5 Analytics Dashboard
- Dashboard web para monitorear performance
- Alertas de videos ultra-virales
- Reportes semanales automáticos

---

# ❓ Apéndice F: FAQs

## ¿Cuánto cuesta mantener este proyecto?

**Respuesta**: ~$200-300/mes inicialmente
- X API Basic: $100/mes
- Google Cloud (TTS + Gemini): $50-100/mes
- Hosting VPS: $20-50/mes
- Break-even: ~200K views/mes en YouTube

## ¿Es legal usar tweets de otros usuarios?

**Respuesta**: Zona gris. Mitigaciones:
- Atribuir claramente (nombre de usuario, link)
- Considerarlo "reacción/comentario" (Fair Use)
- No monetizar hasta tener claridad legal
- Usar solo tweets públicos
- Seguir TOS de X y YouTube

## ¿Qué pasa si me banean de X API?

**Respuesta**: Fallback strategies:
1. Usar scraping ético temporalmente
2. Servicios de terceros (Apify: $50-200/mes)
3. Cambiar a tier superior de API
4. Pivotar a otra fuente (TikTok, Instagram)

## ¿Cuánto tiempo toma generar un video?

**Respuesta**:
- Secuencial: ~5-10 minutos
- Con async TTS: ~2-3 minutos
- Con caching: ~1-2 minutos

## ¿Puedo ejecutar esto en mi laptop?

**Respuesta**: Sí para desarrollo, no para producción
- Desarrollo: OK (genera 1-2 videos manualmente)
- Producción: Requiere VPS 24/7
  - Min specs: 2 vCPU, 4GB RAM, 50GB storage

---

# 🎓 Apéndice G: Recursos de Aprendizaje Adicionales

## Libros Recomendados

1. **Architecture Patterns with Python** (Cosmic Python) - GRATIS online
   - Clean Architecture en Python
   - Domain-Driven Design práctico

2. **Clean Architecture** - Robert C. Martin
   - Principios SOLID
   - Arquitectura de software profesional

3. **Release It!** - Michael Nygard
   - Patterns de resiliencia
   - Production-ready systems

4. **Designing Data-Intensive Applications** - Martin Kleppmann
   - Scaling, performance, reliability

## Cursos Online

1. **ArjanCodes** (YouTube)
   - Clean code en Python
   - Design patterns
   - Testing strategies

2. **mCoding** (YouTube)
   - Python avanzado
   - Performance optimization

3. **Real Python**
   - Tutoriales de alta calidad
   - Proyectos prácticos

## Comunidades

- **r/Python** - Reddit
- **Python Discord**
- **Stack Overflow**
- **Dev.to** - Artículos técnicos

---

# 🏁 Conclusión

## Lo Que Has Construido

Al completar este roadmap, no solo tendrás un **sistema de generación automática de YouTube Shorts funcionando**, sino que habrás dominado:

✅ **Arquitectura de software profesional** (Clean Architecture, DDD, SOLID)
✅ **Ingeniería de resiliencia** (retry, circuit breaker, rate limiting)
✅ **Testing exhaustivo** (unit, integration, e2e, >80% coverage)
✅ **DevOps moderno** (Docker, CI/CD, observability)
✅ **APIs complejas** (OAuth 2.0, quota management, multi-strategy access)
✅ **Multimedia processing** (video, audio, images)
✅ **Production-ready systems** (metrics, alerting, deployment)

## Siguientes Pasos

1. **Validar el concepto**: Publicar 100 videos y medir performance
2. **Optimizar para ROI**: Reducir costos, aumentar views
3. **Escalar**: Múltiples canales, idiomas, nichos
4. **Monetizar**: YouTube Partner, sponsorships, diversificación

## Mantente Actualizado

Este documento es un punto de partida. El landscape de APIs (especialmente X) cambia constantemente. Mantente flexible y adapta tu estrategia según:

- Cambios en X API pricing/features
- Nuevas features de YouTube Shorts
- Tendencias de contenido viral
- Feedback de audiencia

---

## 🎉 ¡Felicidades!

Has llegado al final del roadmap más completo para construir un sistema profesional de generación automática de YouTube Shorts desde tweets virales.

**Esto no es solo un proyecto técnico, es una oportunidad de negocio.**

Con 200K+ views mensuales (totalmente alcanzable), estarás generando $200-1000 USD/mes pasivamente mientras aprendes habilidades que te harán un desarrollador significativamente mejor.

**Ahora deja de leer y empieza a construir. 🚀**

---

**Versión del Roadmap**: 2.0 (Twitter/X Pivot)
**Última actualización**: Enero 2026
**Autor**: Claude (Anthropic)
**Licencia**: Uso educativo libre

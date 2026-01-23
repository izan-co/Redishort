# 🎓 Roadmap Educativo: Redishort v2

## Filosofía del Roadmap

Este no es un simple listado de tareas, sino un **camino de aprendizaje estructurado**. Cada fase está diseñada para enseñarte conceptos fundamentales de ingeniería de software mientras construyes un proyecto real y de calidad profesional.

### Principios Guía

1. **Aprender haciendo**: Cada concepto se acompaña de implementación práctica
2. **Incremental**: Cada fase construye sobre la anterior
3. **Testeable**: Sabrás cuándo algo está bien hecho
4. **Profesional**: Estándares de producción desde el día 1

---

## 📚 Fase 0: Fundamentos y Setup (1 semana)

### Objetivos de Aprendizaje

- Entender arquitectura de aplicaciones modernas
- Dominar herramientas de desarrollo profesional
- Establecer flujo de trabajo eficiente

### Conceptos Clave a Estudiar

| Concepto | Por Qué Es Importante | Recursos |
|----------|----------------------|----------|
| **12-Factor App** | Metodología para apps cloud-native | [12factor.net](https://12factor.net) |
| **Dependency Injection** | Desacopla componentes, facilita testing | Buscar "DI in Python" |
| **Logging estructurado** | Debugging en producción | Aprende `structlog` |
| **Environment-based config** | Diferentes configs para dev/prod | `python-decouple`, `pydantic-settings` |

### Implementación Práctica

#### Paso 1: Estructura de Proyecto Profesional

```
redishort-v2/
├── src/
│   ├── redishort/
│   │   ├── __init__.py
│   │   ├── core/           # Lógica de negocio
│   │   ├── adapters/       # Integraciones externas (Reddit, YouTube)
│   │   ├── domain/         # Modelos de dominio
│   │   └── config/         # Configuración
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
├── docker/
│   ├── Dockerfile.dev
│   └── Dockerfile.prod
├── .github/
│   └── workflows/
├── pyproject.toml          # Gestión de dependencias moderna
├── Makefile                # Comandos comunes
└── README.md
```

**Aprende**: Arquitectura hexagonal (Ports & Adapters)

#### Paso 2: Tooling Moderno

```bash
# Usa pyproject.toml en lugar de requirements.txt
pip install poetry  # Gestión de dependencias moderna

# Herramientas de calidad
poetry add --group dev \
    ruff \          # Linter ultra-rápido (reemplaza flake8, black, isort)
    mypy \          # Type checking
    pytest \        # Testing framework
    pytest-cov \    # Coverage
    pre-commit      # Git hooks automáticos
```

**Aprende**:
- Por qué `pyproject.toml` es mejor que `requirements.txt`
- Qué son los type hints y por qué usarlos
- Cómo funcionan los git hooks

#### Paso 3: Configuración con Pydantic Settings

```python
# src/redishort/config/settings.py
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    """
    Aprende:
    - SecretStr evita logging accidental de secrets
    - Field() documenta y valida cada setting
    - BaseSettings carga automáticamente de .env
    """

    # Reddit API
    reddit_client_id: SecretStr = Field(..., description="Reddit OAuth client ID")
    reddit_client_secret: SecretStr = Field(...)

    # Google AI
    google_api_key: SecretStr = Field(...)

    # YouTube API
    youtube_client_secrets_file: str = Field(default="client_secrets.json")

    # App config
    log_level: str = Field(default="INFO")
    environment: str = Field(default="development")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Singleton global
settings = Settings()
```

**Aprende**:
- Validación automática de configuración
- Fallar rápido (fail-fast) al inicio vs en runtime
- Separación de concerns (config vs lógica)

#### Paso 4: Logging Estructurado

```python
# src/redishort/core/logging.py
import structlog

def setup_logging():
    """
    Aprende:
    - Logs estructurados son parseables (JSON)
    - Facilitan búsqueda en sistemas como ELK
    - Incluyen contexto automáticamente
    """
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer()  # Bonito en dev, JSON en prod
        ],
    )

logger = structlog.get_logger()

# Uso:
logger.info("video_generated", video_id="abc123", duration_sec=45)
# Output: {"event": "video_generated", "video_id": "abc123", ...}
```

### ✅ Criterios de Éxito (Fase 0)

- [ ] Proyecto inicializado con `poetry`
- [ ] `ruff` y `mypy` configurados y pasando
- [ ] `.env.example` documentado con todas las variables
- [ ] Logging estructurado funcionando
- [ ] Pre-commit hooks instalados
- [ ] README con instrucciones de setup

### 📖 Recursos de Aprendizaje

- [Real Python: Project Structure](https://realpython.com/python-application-layouts/)
- [Pydantic Settings Docs](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [Structlog Tutorial](https://www.structlog.org/en/stable/getting-started.html)

---

## 🏗️ Fase 1: Core Architecture (2 semanas)

### Objetivos de Aprendizaje

- Diseño orientado a dominio (DDD)
- Principios SOLID
- Dependency Injection en Python
- Testing unitario efectivo

### Conceptos Clave a Estudiar

| Concepto | Por Qué | Ejemplo en Nuestro Proyecto |
|----------|---------|----------------------------|
| **Domain Models** | Representan tu lógica de negocio sin dependencias externas | `RedditStory`, `VideoScript`, `GeneratedVideo` |
| **Repository Pattern** | Abstrae persistencia de datos | `StoryRepository`, `VideoRepository` |
| **Service Layer** | Orquesta casos de uso | `VideoGenerationService` |
| **Dependency Injection** | Facilita testing y flexibilidad | Constructor injection |

### Implementación Práctica

#### Paso 1: Modelos de Dominio (Domain Models)

```python
# src/redishort/domain/models.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum

class VideoStatus(Enum):
    """
    Aprende: Enums son mejores que strings mágicos
    - Type-safe
    - Autocomplete en IDE
    - Imposible de escribir mal
    """
    PENDING = "pending"
    PROCESSING = "processing"
    GENERATED = "generated"
    UPLOADED = "uploaded"
    FAILED = "failed"

@dataclass(frozen=True)  # Aprende: Immutability por defecto
class RedditStory:
    """
    Aprende: Domain model sin dependencias externas
    - No importa praw, requests, ni nada externo
    - Puede testarse sin mocks complejos
    - Representa SOLO la lógica de negocio
    """
    id: str
    title: str
    selftext: str
    author: str
    score: int
    created_utc: datetime
    permalink: str

    def is_suitable_for_video(self) -> bool:
        """Business logic: ¿Esta historia sirve para video?"""
        return (
            len(self.title) >= 20 and
            len(self.selftext) >= 100 and
            self.score >= 50 and
            not any(word in self.title.lower() for word in ['nsfw', 'removed'])
        )

@dataclass
class VideoScript:
    """
    Aprende: Separar datos de comportamiento
    - Este es un Value Object (sin identidad propia)
    - Inmutable después de creación
    """
    story_id: str
    segments: List[str]
    total_duration_sec: float
    voice_config: dict = field(default_factory=dict)

    def __post_init__(self):
        if len(self.segments) == 0:
            raise ValueError("Script must have at least one segment")

@dataclass
class GeneratedVideo:
    """Entity con identidad y ciclo de vida"""
    id: str
    story_id: str
    script_id: str
    video_path: str
    status: VideoStatus
    created_at: datetime = field(default_factory=datetime.utcnow)
    uploaded_at: Optional[datetime] = None
    youtube_id: Optional[str] = None

    def mark_as_uploaded(self, youtube_id: str) -> None:
        """
        Aprende: Métodos que mantienen invariantes
        - No puedes marcar como uploaded sin youtube_id
        - Estado siempre válido
        """
        self.status = VideoStatus.UPLOADED
        self.youtube_id = youtube_id
        self.uploaded_at = datetime.utcnow()
```

**Aprende**:
- Domain models no tienen dependencias externas
- Inmutabilidad previene bugs
- Business logic vive en los modelos

#### Paso 2: Repository Pattern (Abstracción de Datos)

```python
# src/redishort/domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from .models import RedditStory, GeneratedVideo, VideoStatus

class StoryRepository(ABC):
    """
    Aprende: Interface (Protocol) vs Implementation
    - Define QUÉ hacer, no CÓMO
    - Permite múltiples implementaciones (SQLite, Postgres, Mock)
    - Facilita testing (inyectas un FakeRepository)
    """

    @abstractmethod
    def get_by_id(self, story_id: str) -> Optional[RedditStory]:
        pass

    @abstractmethod
    def save(self, story: RedditStory) -> None:
        pass

    @abstractmethod
    def get_unprocessed_stories(self, limit: int = 10) -> List[RedditStory]:
        pass

class VideoRepository(ABC):
    @abstractmethod
    def save(self, video: GeneratedVideo) -> None:
        pass

    @abstractmethod
    def get_by_status(self, status: VideoStatus) -> List[GeneratedVideo]:
        pass

    @abstractmethod
    def update_status(self, video_id: str, status: VideoStatus) -> None:
        pass


# src/redishort/adapters/sqlite_repository.py
import sqlite3
from ..domain.repositories import StoryRepository, VideoRepository
from ..domain.models import RedditStory, GeneratedVideo

class SQLiteStoryRepository(StoryRepository):
    """
    Aprende: Implementación concreta
    - Maneja detalles de SQLite
    - Core domain no sabe que existe SQLite
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS stories (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    selftext TEXT NOT NULL,
                    author TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    created_utc TIMESTAMP NOT NULL,
                    permalink TEXT NOT NULL,
                    processed BOOLEAN DEFAULT 0
                )
            """)

    def get_by_id(self, story_id: str) -> Optional[RedditStory]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM stories WHERE id = ?", (story_id,)
            ).fetchone()
            return self._row_to_story(row) if row else None

    def save(self, story: RedditStory) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO stories
                (id, title, selftext, author, score, created_utc, permalink)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                story.id, story.title, story.selftext,
                story.author, story.score, story.created_utc, story.permalink
            ))

    def _row_to_story(self, row) -> RedditStory:
        return RedditStory(
            id=row['id'],
            title=row['title'],
            selftext=row['selftext'],
            author=row['author'],
            score=row['score'],
            created_utc=datetime.fromisoformat(row['created_utc']),
            permalink=row['permalink']
        )
```

**Aprende**:
- Separación entre interface y implementación
- Puedes cambiar SQLite por Postgres sin tocar domain logic
- Tests unitarios no necesitan base de datos real

#### Paso 3: Service Layer (Casos de Uso)

```python
# src/redishort/core/services.py
from typing import Protocol
import structlog
from ..domain.models import RedditStory, VideoScript, GeneratedVideo, VideoStatus
from ..domain.repositories import StoryRepository, VideoRepository

logger = structlog.get_logger()

class ContentFetcher(Protocol):
    """
    Aprende: Protocol en lugar de ABC
    - Más pythónico (duck typing)
    - No requiere herencia explícita
    """
    def fetch_stories(self, subreddit: str, limit: int) -> list[RedditStory]:
        ...

class ScriptGenerator(Protocol):
    def generate_script(self, story: RedditStory) -> VideoScript:
        ...

class VideoRenderer(Protocol):
    def render_video(self, script: VideoScript) -> str:  # Returns path
        ...

class VideoUploader(Protocol):
    def upload(self, video_path: str, title: str) -> str:  # Returns YouTube ID
        ...


class VideoGenerationService:
    """
    Aprende: Service Layer orquesta casos de uso
    - No contiene lógica de negocio (está en domain models)
    - No sabe de SQLite, Reddit API, etc (usa abstracciones)
    - Coordina múltiples componentes
    """

    def __init__(
        self,
        story_repo: StoryRepository,
        video_repo: VideoRepository,
        content_fetcher: ContentFetcher,
        script_generator: ScriptGenerator,
        video_renderer: VideoRenderer,
        video_uploader: VideoUploader,
    ):
        """
        Aprende: Dependency Injection via constructor
        - Todas las dependencias son explícitas
        - Fácil de testear (inyectas mocks)
        - No hay imports de implementaciones concretas
        """
        self.story_repo = story_repo
        self.video_repo = video_repo
        self.content_fetcher = content_fetcher
        self.script_generator = script_generator
        self.video_renderer = video_renderer
        self.video_uploader = video_uploader
        self.logger = logger.bind(service="video_generation")

    def process_new_stories(self, subreddit: str) -> int:
        """
        Caso de uso: Procesar historias nuevas de Reddit
        Returns: Número de videos generados
        """
        self.logger.info("fetching_stories", subreddit=subreddit)

        # Fetch stories from Reddit
        stories = self.content_fetcher.fetch_stories(subreddit, limit=10)

        # Filter suitable ones
        suitable = [s for s in stories if s.is_suitable_for_video()]
        self.logger.info("stories_filtered", total=len(stories), suitable=len(suitable))

        # Save to database
        for story in suitable:
            self.story_repo.save(story)

        return len(suitable)

    def generate_video_from_story(self, story_id: str) -> GeneratedVideo:
        """
        Caso de uso: Generar video de una historia

        Aprende: Este método coordina el workflow completo
        - Cada paso puede fallar independientemente
        - Estado se guarda entre pasos
        - Fácil de testear cada paso
        """
        story = self.story_repo.get_by_id(story_id)
        if not story:
            raise ValueError(f"Story {story_id} not found")

        # Create video entity
        video = GeneratedVideo(
            id=f"video_{story_id}",
            story_id=story_id,
            script_id="",
            video_path="",
            status=VideoStatus.PENDING
        )
        self.video_repo.save(video)

        try:
            # Generate script
            self.logger.info("generating_script", story_id=story_id)
            script = self.script_generator.generate_script(story)

            # Render video
            self.logger.info("rendering_video", story_id=story_id)
            video.video_path = self.video_renderer.render_video(script)
            video.status = VideoStatus.GENERATED
            self.video_repo.save(video)

            return video

        except Exception as e:
            self.logger.error("video_generation_failed", story_id=story_id, error=str(e))
            video.status = VideoStatus.FAILED
            self.video_repo.save(video)
            raise

    def upload_pending_videos(self) -> int:
        """
        Caso de uso: Subir videos pendientes a YouTube
        """
        videos = self.video_repo.get_by_status(VideoStatus.GENERATED)
        uploaded_count = 0

        for video in videos:
            try:
                story = self.story_repo.get_by_id(video.story_id)
                youtube_id = self.video_uploader.upload(
                    video.video_path,
                    title=story.title
                )

                video.mark_as_uploaded(youtube_id)
                self.video_repo.save(video)
                uploaded_count += 1

            except Exception as e:
                self.logger.error("upload_failed", video_id=video.id, error=str(e))

        return uploaded_count
```

**Aprende**:
- Service layer es el "cerebro" de la aplicación
- Coordina domain models y adapters
- Fácil de testear porque todo es inyectado

#### Paso 4: Testing (Lo Más Importante)

```python
# tests/unit/test_video_generation_service.py
import pytest
from datetime import datetime
from redishort.domain.models import RedditStory, VideoStatus
from redishort.core.services import VideoGenerationService

class FakeStoryRepository:
    """
    Aprende: Fake > Mock en tests unitarios
    - Más realista que mocks
    - Comportamiento verificable
    - No acoplado a implementación
    """
    def __init__(self):
        self.stories = {}

    def save(self, story):
        self.stories[story.id] = story

    def get_by_id(self, story_id):
        return self.stories.get(story_id)

class FakeVideoRepository:
    def __init__(self):
        self.videos = {}

    def save(self, video):
        self.videos[video.id] = video

    def get_by_status(self, status):
        return [v for v in self.videos.values() if v.status == status]

class FakeContentFetcher:
    def fetch_stories(self, subreddit, limit):
        # Return deterministic test data
        return [
            RedditStory(
                id="test123",
                title="Great story for testing",
                selftext="This is a long enough story for video generation",
                author="testuser",
                score=100,
                created_utc=datetime.utcnow(),
                permalink="/r/test/123"
            )
        ]

class FakeScriptGenerator:
    def generate_script(self, story):
        return VideoScript(
            story_id=story.id,
            segments=["Segment 1", "Segment 2"],
            total_duration_sec=60.0
        )

class FakeVideoRenderer:
    def render_video(self, script):
        return f"/tmp/video_{script.story_id}.mp4"

class FakeVideoUploader:
    def upload(self, video_path, title):
        return "youtube_123"


@pytest.fixture
def service():
    """
    Aprende: Fixtures para setup de tests
    - Reutilizable en múltiples tests
    - Dependency injection para tests
    """
    return VideoGenerationService(
        story_repo=FakeStoryRepository(),
        video_repo=FakeVideoRepository(),
        content_fetcher=FakeContentFetcher(),
        script_generator=FakeScriptGenerator(),
        video_renderer=FakeVideoRenderer(),
        video_uploader=FakeVideoUploader(),
    )


def test_process_new_stories(service):
    """
    Aprende: Test del happy path
    - Nombre descriptivo (no test_1, test_2)
    - Arrange, Act, Assert pattern
    """
    # Act
    count = service.process_new_stories("askreddit")

    # Assert
    assert count == 1
    story = service.story_repo.get_by_id("test123")
    assert story is not None
    assert story.title == "Great story for testing"


def test_generate_video_from_story(service):
    """Test video generation workflow"""
    # Arrange
    story = RedditStory(
        id="story123",
        title="Test Story" * 5,  # Long enough
        selftext="Content" * 50,  # Long enough
        author="test",
        score=100,
        created_utc=datetime.utcnow(),
        permalink="/r/test/1"
    )
    service.story_repo.save(story)

    # Act
    video = service.generate_video_from_story("story123")

    # Assert
    assert video.status == VideoStatus.GENERATED
    assert video.video_path.endswith(".mp4")


def test_generate_video_from_nonexistent_story(service):
    """
    Aprende: Test de error paths
    - Igual de importantes que happy paths
    - Usa pytest.raises para excepciones
    """
    with pytest.raises(ValueError, match="Story .* not found"):
        service.generate_video_from_story("nonexistent")


def test_upload_pending_videos(service):
    """Test upload workflow"""
    # Arrange: Create a generated video
    story = RedditStory(id="s1", title="T"*20, selftext="C"*100,
                        author="a", score=50,
                        created_utc=datetime.utcnow(), permalink="/r/t/1")
    service.story_repo.save(story)

    video = GeneratedVideo(
        id="v1",
        story_id="s1",
        script_id="sc1",
        video_path="/tmp/video.mp4",
        status=VideoStatus.GENERATED
    )
    service.video_repo.save(video)

    # Act
    count = service.upload_pending_videos()

    # Assert
    assert count == 1
    uploaded_video = service.video_repo.videos["v1"]
    assert uploaded_video.status == VideoStatus.UPLOADED
    assert uploaded_video.youtube_id == "youtube_123"
```

**Aprende**:
- Fakes > Mocks para tests más robustos
- Tests unitarios deben ser rápidos (sin I/O real)
- Testa tanto happy paths como error paths

### ✅ Criterios de Éxito (Fase 1)

- [ ] Domain models sin dependencias externas
- [ ] Repository interfaces definidas
- [ ] Service layer con dependency injection
- [ ] Tests unitarios con >80% coverage
- [ ] `mypy` pasa sin errores (type safety)
- [ ] Documentación de conceptos aprendidos

### 📖 Recursos de Aprendizaje

- [Architecture Patterns with Python](https://www.cosmicpython.com/) (EXCELENTE libro, gratis online)
- [Clean Architecture (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Dependency Injection in Python](https://www.youtube.com/watch?v=2ejbLVkCndI)
- [pytest Documentation](https://docs.pytest.org/)

---

## 🔌 Fase 2: Adapters - Reddit & AI (1.5 semanas)

### Objetivos de Aprendizaje

- Implementar adapters para APIs externas
- Rate limiting y retry logic robustos
- Circuit breaker pattern
- Error handling estratégico

### Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **Adapter Pattern** | Adapta APIs externas a tu domain | `RedditAdapter`, `GeminiAdapter` |
| **Retry with exponential backoff** | Resiliencia ante errores transitorios | `tenacity` |
| **Circuit Breaker** | Previene cascadas de fallos | `pybreaker` |
| **Rate Limiting** | Evita ban por exceso de requests | `ratelimit` |

### Implementación Práctica

#### Paso 1: Reddit Content Fetcher

```python
# src/redishort/adapters/reddit_adapter.py
import praw
from tenacity import retry, stop_after_attempt, wait_exponential
from ratelimit import limits, sleep_and_retry
import structlog
from ..domain.models import RedditStory
from ..config.settings import settings

logger = structlog.get_logger()

class RedditAdapter:
    """
    Aprende: Adapter pattern
    - Traduce API de praw a nuestros domain models
    - Encapsula toda la complejidad de Reddit API
    - Si cambiamos a otra fuente, solo cambiamos este adapter
    """

    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=settings.reddit_client_id.get_secret_value(),
            client_secret=settings.reddit_client_secret.get_secret_value(),
            user_agent=settings.reddit_user_agent,
        )
        self.logger = logger.bind(adapter="reddit")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    @sleep_and_retry
    @limits(calls=60, period=60)  # 60 requests per minute
    def fetch_stories(self, subreddit: str, limit: int = 10) -> list[RedditStory]:
        """
        Aprende: Defensive programming
        - @retry: Reintenta en errores transitorios
        - @limits: Rate limiting (60 req/min)
        - @sleep_and_retry: Espera si excede límite

        Si Reddit está caído 30 segundos, esto reintenta automáticamente.
        Si mandas demasiadas requests, espera automáticamente.
        """
        try:
            self.logger.info("fetching_stories", subreddit=subreddit, limit=limit)

            submissions = self.reddit.subreddit(subreddit).hot(limit=limit * 2)
            stories = []

            for submission in submissions:
                # Skip stickied posts, removed, etc.
                if submission.stickied or submission.removed_by_category:
                    continue

                story = RedditStory(
                    id=submission.id,
                    title=submission.title,
                    selftext=submission.selftext,
                    author=str(submission.author),
                    score=submission.score,
                    created_utc=datetime.fromtimestamp(submission.created_utc),
                    permalink=submission.permalink
                )

                if story.is_suitable_for_video():
                    stories.append(story)

                if len(stories) >= limit:
                    break

            self.logger.info("stories_fetched", count=len(stories))
            return stories

        except praw.exceptions.PRAWException as e:
            self.logger.error("reddit_api_error", error=str(e))
            raise
        except Exception as e:
            self.logger.error("unexpected_error", error=str(e))
            raise
```

#### Paso 2: Gemini Script Generator con Circuit Breaker

```python
# src/redishort/adapters/gemini_adapter.py
import google.generativeai as genai
from pybreaker import CircuitBreaker
from tenacity import retry, stop_after_attempt, wait_exponential
import structlog
from ..domain.models import RedditStory, VideoScript
from ..config.settings import settings

logger = structlog.get_logger()

# Circuit breaker: Si 5 requests fallan, abre el circuito por 60 segundos
gemini_breaker = CircuitBreaker(
    fail_max=5,
    reset_timeout=60,
    name="gemini_api"
)

class GeminiAdapter:
    """
    Aprende: Circuit Breaker Pattern
    - Si Gemini API falla repetidamente, dejamos de intentar temporalmente
    - Permite que el servicio se recupere
    - Previene "thundering herd" problem
    """

    def __init__(self):
        genai.configure(api_key=settings.google_api_key.get_secret_value())

        # Aprende: Safety settings explícitos y documentados
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
        self.logger = logger.bind(adapter="gemini")

    @gemini_breaker
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=4, max=30)
    )
    def generate_script(self, story: RedditStory) -> VideoScript:
        """
        Aprende: Retry + Circuit Breaker
        - Retry: Errores transitorios (network glitch)
        - Circuit Breaker: Errores sistemáticos (API down)

        Si el circuit breaker está abierto, falla inmediatamente sin retry.
        """
        try:
            prompt = self._build_prompt(story)

            self.logger.info("generating_script", story_id=story.id)
            response = self.model.generate_content(prompt)

            # Parse response into segments
            segments = self._parse_segments(response.text)

            return VideoScript(
                story_id=story.id,
                segments=segments,
                total_duration_sec=len(segments) * 5.0,  # Estimate
                voice_config={"model": "en-US-Studio-O"}
            )

        except genai.types.BlockedPromptException as e:
            self.logger.warning("prompt_blocked", story_id=story.id, reason=str(e))
            raise
        except genai.types.StopCandidateException as e:
            self.logger.warning("response_stopped", story_id=story.id, reason=str(e))
            raise
        except Exception as e:
            self.logger.error("gemini_error", story_id=story.id, error=str(e))
            raise

    def _build_prompt(self, story: RedditStory) -> str:
        """
        Aprende: Prompt engineering como código
        - Versionado en git
        - Testeable
        - Documentado
        """
        return f"""
You are a YouTube Shorts scriptwriter. Convert this Reddit story into engaging segments.

Story Title: {story.title}
Story Content: {story.selftext}

Requirements:
- 5-8 segments of 10-15 seconds each
- Start with a hook
- Use conversational language
- End with a call-to-action

Output format:
SEGMENT_1: [text]
SEGMENT_2: [text]
...
"""

    def _parse_segments(self, response_text: str) -> list[str]:
        """Parse Gemini response into segments"""
        segments = []
        for line in response_text.split('\n'):
            if line.strip().startswith('SEGMENT_'):
                # Extract text after colon
                text = line.split(':', 1)[1].strip()
                segments.append(text)

        if not segments:
            raise ValueError("No segments found in Gemini response")

        return segments
```

#### Paso 3: Testing de Adapters (Integration Tests)

```python
# tests/integration/test_reddit_adapter.py
import pytest
from redishort.adapters.reddit_adapter import RedditAdapter

@pytest.mark.integration
def test_reddit_adapter_fetch_stories():
    """
    Aprende: Integration tests
    - Tocan APIs reales (lentos)
    - Usan @pytest.mark.integration para separarlos
    - Corren en CI pero no en cada save del IDE

    Run: pytest -m integration
    """
    adapter = RedditAdapter()

    stories = adapter.fetch_stories("askreddit", limit=5)

    assert len(stories) > 0
    assert all(s.is_suitable_for_video() for s in stories)
    assert all(s.score > 0 for s in stories)


# tests/unit/test_gemini_adapter.py
from unittest.mock import Mock, patch
from redishort.adapters.gemini_adapter import GeminiAdapter
from redishort.domain.models import RedditStory

def test_gemini_adapter_generate_script():
    """
    Aprende: Mocking de APIs externas en unit tests
    - Rápido (no toca red)
    - Determinista (siempre retorna lo mismo)
    - No consume quota de API
    """
    adapter = GeminiAdapter()

    # Mock the Gemini API
    mock_response = Mock()
    mock_response.text = """
SEGMENT_1: Hook segment
SEGMENT_2: Middle segment
SEGMENT_3: End segment
"""

    with patch.object(adapter.model, 'generate_content', return_value=mock_response):
        story = RedditStory(
            id="test",
            title="Test Story" * 5,
            selftext="Content" * 50,
            author="test",
            score=100,
            created_utc=datetime.utcnow(),
            permalink="/r/test/1"
        )

        script = adapter.generate_script(story)

        assert len(script.segments) == 3
        assert script.story_id == "test"


def test_circuit_breaker_opens_on_failures():
    """
    Aprende: Testing de circuit breaker
    - Simula múltiples fallos
    - Verifica que el circuito se abre
    """
    adapter = GeminiAdapter()

    # Mock to always fail
    with patch.object(adapter.model, 'generate_content', side_effect=Exception("API down")):
        story = RedditStory(...)  # Valid story

        # First 5 should retry and fail
        for _ in range(5):
            with pytest.raises(Exception):
                adapter.generate_script(story)

        # 6th should fail immediately (circuit open)
        with pytest.raises(CircuitBreakerError):
            adapter.generate_script(story)
```

### ✅ Criterios de Éxito (Fase 2)

- [ ] Reddit adapter con rate limiting funcionando
- [ ] Gemini adapter con retry y circuit breaker
- [ ] Integration tests pasando
- [ ] Circuit breaker testeado
- [ ] Logging de todos los errores externos

### 📖 Recursos de Aprendizaje

- [tenacity documentation](https://tenacity.readthedocs.io/)
- [pybreaker documentation](https://github.com/danielfm/pybreaker)
- [Release It! (libro sobre resiliencia)](https://pragprog.com/titles/mnee2/release-it-second-edition/)

---

## 🎬 Fase 3: Video Generation Pipeline (2 semanas)

### Objetivos de Aprendizaje

- Pipeline de procesamiento asíncrono
- Manejo de recursos multimedia (memory management)
- Composición de video programática
- Optimización de rendimiento

### Conceptos Clave

| Concepto | Por Qué | Implementación |
|----------|---------|----------------|
| **Pipeline Pattern** | Separa etapas de procesamiento | TTS → Subtitle → Composition |
| **Resource Management** | Evita memory leaks con videos | Context managers |
| **Async/Concurrency** | Procesa múltiples videos en paralelo | `asyncio` |

### Implementación Práctica

#### Paso 1: TTS Service

```python
# src/redishort/adapters/tts_adapter.py
from pathlib import Path
from google.cloud import texttospeech
import structlog
from ..domain.models import VideoScript

logger = structlog.get_logger()

class TTSAdapter:
    """
    Aprende: Separación de concerns
    - Solo hace TTS, nada más
    - Retorna paths de archivos
    - No sabe qué pasa después
    """

    def __init__(self, output_dir: Path):
        self.client = texttospeech.TextToSpeechClient()
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logger.bind(adapter="tts")

    def generate_audio_for_script(self, script: VideoScript) -> list[Path]:
        """
        Generate audio file for each segment

        Returns: List of audio file paths (one per segment)

        Aprende:
        - Retorna paths, no bytes (más fácil de testear/debuggear)
        - Una función, una responsabilidad
        """
        audio_paths = []

        for idx, segment in enumerate(script.segments):
            audio_path = self._generate_segment_audio(
                segment,
                output_path=self.output_dir / f"{script.story_id}_seg{idx}.mp3"
            )
            audio_paths.append(audio_path)

        self.logger.info("audio_generated", story_id=script.story_id, segments=len(audio_paths))
        return audio_paths

    def _generate_segment_audio(self, text: str, output_path: Path) -> Path:
        """Generate audio for single segment"""
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Studio-O",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1.05,
            pitch=0.0
        )

        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        output_path.write_bytes(response.audio_content)
        return output_path
```

#### Paso 2: Video Composition (con Resource Management)

```python
# src/redishort/adapters/video_renderer.py
from pathlib import Path
from contextlib import contextmanager
from moviepy.editor import (
    VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip,
    concatenate_videoclips
)
import structlog
from ..domain.models import VideoScript

logger = structlog.get_logger()

@contextmanager
def managed_clip(clip):
    """
    Aprende: Context manager para cleanup automático
    - MoviePy tiene memory leaks si no cierras clips
    - Context manager garantiza cleanup incluso si hay excepciones
    """
    try:
        yield clip
    finally:
        if clip:
            clip.close()


class VideoRenderer:
    """
    Aprende: Pipeline de procesamiento
    1. Load background video
    2. Add audio
    3. Add subtitles
    4. Compose
    5. Export
    """

    def __init__(self, assets_dir: Path, output_dir: Path):
        self.assets_dir = assets_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logger.bind(adapter="video_renderer")

    def render_video(
        self,
        script: VideoScript,
        audio_paths: list[Path]
    ) -> Path:
        """
        Render complete video from script and audio

        Aprende: High-level orchestration
        - Delega detalles a métodos privados
        - Error handling en cada paso
        - Resource cleanup garantizado
        """
        output_path = self.output_dir / f"{script.story_id}.mp4"

        try:
            self.logger.info("rendering_video", story_id=script.story_id)

            # Load background video
            with managed_clip(self._load_background()) as background:

                # Create segment clips with audio and subtitles
                segment_clips = []
                for idx, (segment_text, audio_path) in enumerate(zip(script.segments, audio_paths)):
                    segment_clip = self._create_segment_clip(
                        background=background,
                        text=segment_text,
                        audio_path=audio_path
                    )
                    segment_clips.append(segment_clip)

                # Concatenate all segments
                with managed_clip(concatenate_videoclips(segment_clips)) as final:
                    final.write_videofile(
                        str(output_path),
                        codec='libx264',
                        audio_codec='aac',
                        fps=30,
                        preset='medium',  # Aprende: balance entre calidad y velocidad
                        threads=4
                    )

            # Clean up segment clips
            for clip in segment_clips:
                clip.close()

            self.logger.info("video_rendered", path=str(output_path))
            return output_path

        except Exception as e:
            self.logger.error("render_failed", story_id=script.story_id, error=str(e))
            raise

    def _load_background(self) -> VideoFileClip:
        """Load random background video"""
        backgrounds = list(self.assets_dir.glob("backgrounds/*.mp4"))
        if not backgrounds:
            raise ValueError("No background videos found")

        import random
        background_path = random.choice(backgrounds)
        return VideoFileClip(str(background_path))

    def _create_segment_clip(
        self,
        background: VideoFileClip,
        text: str,
        audio_path: Path
    ) -> VideoFileClip:
        """
        Create video clip for one segment with audio and subtitles

        Aprende: Composition pattern
        - Background + Audio + Text = Final clip
        """
        # Load audio
        audio = AudioFileClip(str(audio_path))
        duration = audio.duration

        # Crop background to match audio duration
        start_time = 0  # Could randomize
        segment_bg = background.subclip(start_time, start_time + duration)

        # Create subtitle text clip
        subtitle = TextClip(
            text,
            fontsize=60,
            color='white',
            stroke_color='black',
            stroke_width=2,
            font='Arial-Bold',
            method='caption',
            size=(segment_bg.w * 0.9, None),  # 90% of video width
        ).set_duration(duration).set_position(('center', 'bottom'))

        # Composite: background + subtitle
        composite = CompositeVideoClip([segment_bg, subtitle])

        # Add audio
        composite = composite.set_audio(audio)

        return composite
```

#### Paso 3: Async Pipeline (Bonus: Performance)

```python
# src/redishort/core/async_video_pipeline.py
import asyncio
from pathlib import Path
import structlog
from ..domain.models import VideoScript, GeneratedVideo, VideoStatus
from ..domain.repositories import VideoRepository
from ..adapters.tts_adapter import TTSAdapter
from ..adapters.video_renderer import VideoRenderer

logger = structlog.get_logger()

class AsyncVideoPipeline:
    """
    Aprende: Async para I/O-bound operations
    - TTS API calls son I/O-bound (esperan red)
    - Podemos generar audio de 5 segmentos en paralelo
    - Video rendering es CPU-bound (no se beneficia de async)
    """

    def __init__(
        self,
        tts_adapter: TTSAdapter,
        video_renderer: VideoRenderer,
        video_repo: VideoRepository
    ):
        self.tts = tts_adapter
        self.renderer = video_renderer
        self.video_repo = video_repo
        self.logger = logger.bind(pipeline="async_video")

    async def generate_video_async(self, script: VideoScript) -> GeneratedVideo:
        """
        Aprende: Async pipeline
        1. Generate audio for all segments in parallel (async)
        2. Render video (sync, CPU-bound)
        3. Update database
        """
        video = GeneratedVideo(
            id=f"video_{script.story_id}",
            story_id=script.story_id,
            script_id=script.story_id,
            video_path="",
            status=VideoStatus.PROCESSING
        )
        self.video_repo.save(video)

        try:
            # Generate audio for all segments in parallel
            self.logger.info("generating_audio_async", story_id=script.story_id)
            audio_paths = await self._generate_audio_parallel(script)

            # Render video (CPU-bound, run in thread pool)
            self.logger.info("rendering_video", story_id=script.story_id)
            video_path = await asyncio.to_thread(
                self.renderer.render_video,
                script,
                audio_paths
            )

            video.video_path = str(video_path)
            video.status = VideoStatus.GENERATED
            self.video_repo.save(video)

            return video

        except Exception as e:
            self.logger.error("pipeline_failed", story_id=script.story_id, error=str(e))
            video.status = VideoStatus.FAILED
            self.video_repo.save(video)
            raise

    async def _generate_audio_parallel(self, script: VideoScript) -> list[Path]:
        """
        Generate audio for all segments in parallel

        Aprende: asyncio.gather para paralelización
        - Lanza todas las requests TTS al mismo tiempo
        - Espera a que todas terminen
        - 5 segmentos: 5x más rápido que secuencial
        """
        tasks = [
            asyncio.to_thread(
                self.tts._generate_segment_audio,
                segment,
                self.tts.output_dir / f"{script.story_id}_seg{idx}.mp3"
            )
            for idx, segment in enumerate(script.segments)
        ]

        audio_paths = await asyncio.gather(*tasks)
        return list(audio_paths)
```

### ✅ Criterios de Éxito (Fase 3)

- [ ] TTS adapter funcionando
- [ ] Video renderer con resource management
- [ ] No memory leaks (verifica con `memory_profiler`)
- [ ] Async pipeline genera videos 3-5x más rápido
- [ ] Videos de calidad (30fps, 1080x1920)

### 📖 Recursos de Aprendizaje

- [MoviePy Documentation](https://zulko.github.io/moviepy/)
- [Real Python: Async IO](https://realpython.com/async-io-python/)
- [Python Context Managers](https://realpython.com/python-with-statement/)

---

## 📤 Fase 4: YouTube Upload & Scheduler (1 semana)

### Objetivos de Aprendizaje

- OAuth 2.0 flow robusto
- Quota management
- Job scheduling
- Observability

### Implementación Práctica

#### Paso 1: YouTube Uploader con Quota Tracking

```python
# src/redishort/adapters/youtube_adapter.py
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path
import structlog

logger = structlog.get_logger()

class YouTubeQuotaExceeded(Exception):
    """Aprende: Custom exceptions para casos específicos"""
    pass

class YouTubeAdapter:
    """
    Aprende: OAuth 2.0 + Quota management
    - Maneja refresh de tokens automáticamente
    - Trackea quota usage
    - Falla gracefully cuando se acaba quota
    """

    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    UPLOAD_COST = 1600  # YouTube API quota cost
    DAILY_QUOTA = 10000

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
        2. Si expiró, refresca automáticamente
        3. Si no existe, ejecuta OAuth flow
        """
        creds = None

        if self.token_file.exists():
            creds = Credentials.from_authorized_user_file(
                str(self.token_file),
                self.SCOPES
            )

        # Refresh if expired
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        # New OAuth flow if no creds
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(self.credentials_file),
                self.SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save credentials
        self.token_file.write_text(creds.to_json())

        return build('youtube', 'v3', credentials=creds)

    def upload_video(
        self,
        video_path: Path,
        title: str,
        description: str,
        tags: list[str]
    ) -> str:
        """
        Upload video to YouTube with quota checking

        Returns: YouTube video ID

        Aprende: Fail-fast con quota
        - Verifica quota ANTES de subir
        - Evita desperdiciar bandwidth
        """
        if self.quota_used_today + self.UPLOAD_COST > self.DAILY_QUOTA:
            raise YouTubeQuotaExceeded(
                f"Daily quota exceeded: {self.quota_used_today}/{self.DAILY_QUOTA}"
            )

        try:
            self.logger.info("uploading_video", title=title)

            body = {
                'snippet': {
                    'title': title[:100],  # YouTube limit
                    'description': description,
                    'tags': tags,
                    'categoryId': '24'  # Entertainment
                },
                'status': {
                    'privacyStatus': 'private',  # Aprende: Upload as private first
                    'selfDeclaredMadeForKids': False
                }
            }

            media = MediaFileUpload(
                str(video_path),
                chunksize=1024*1024,  # 1MB chunks
                resumable=True
            )

            request = self.youtube.videos().insert(
                part='snippet,status',
                body=body,
                media_body=media
            )

            response = self._execute_upload_with_retry(request)
            video_id = response['id']

            # Track quota usage
            self.quota_used_today += self.UPLOAD_COST
            self._save_quota_usage()

            self.logger.info("video_uploaded", video_id=video_id, quota_used=self.quota_used_today)
            return video_id

        except Exception as e:
            self.logger.error("upload_failed", error=str(e))
            raise

    def _execute_upload_with_retry(self, request):
        """
        Aprende: Resumable uploads
        - Si falla en 80%, reintenta desde 80%
        - No re-sube todo el video
        """
        response = None
        error = None
        retry = 0

        while response is None:
            try:
                status, response = request.next_chunk()
                if status:
                    self.logger.info("upload_progress", percent=int(status.progress() * 100))
            except Exception as e:
                error = e
                if retry < 3:
                    retry += 1
                    self.logger.warning("upload_retry", attempt=retry, error=str(e))
                    time.sleep(2 ** retry)
                else:
                    raise

        return response
```

#### Paso 2: Scheduler con APScheduler

```python
# src/redishort/core/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import structlog
from .services import VideoGenerationService

logger = structlog.get_logger()

class VideoScheduler:
    """
    Aprende: Job scheduling
    - Ejecuta tareas periódicamente
    - Cron syntax para horarios
    - Async-aware
    """

    def __init__(self, service: VideoGenerationService):
        self.service = service
        self.scheduler = AsyncIOScheduler()
        self.logger = logger.bind(component="scheduler")

    def setup_jobs(self):
        """
        Configure scheduled jobs

        Aprende: Cron syntax
        - "0 */3 * * *" = Every 3 hours
        - "0 9 * * *" = Daily at 9 AM
        """
        # Fetch new stories every 3 hours
        self.scheduler.add_job(
            self._fetch_stories_job,
            trigger=CronTrigger(hour="*/3"),
            id="fetch_stories",
            name="Fetch Reddit stories",
            max_instances=1  # No overlapping runs
        )

        # Generate videos every hour
        self.scheduler.add_job(
            self._generate_videos_job,
            trigger=CronTrigger(minute=0),
            id="generate_videos",
            name="Generate videos from stories"
        )

        # Upload videos daily at 9 AM
        self.scheduler.add_job(
            self._upload_videos_job,
            trigger=CronTrigger(hour=9),
            id="upload_videos",
            name="Upload videos to YouTube"
        )

        self.logger.info("jobs_scheduled", count=len(self.scheduler.get_jobs()))

    async def _fetch_stories_job(self):
        """Job: Fetch new stories"""
        try:
            count = self.service.process_new_stories("askreddit")
            self.logger.info("stories_fetched", count=count)
        except Exception as e:
            self.logger.error("fetch_job_failed", error=str(e))

    async def _generate_videos_job(self):
        """Job: Generate videos from unprocessed stories"""
        try:
            # Get pending stories
            stories = self.service.story_repo.get_unprocessed_stories(limit=5)

            for story in stories:
                await self.service.generate_video_from_story(story.id)

            self.logger.info("videos_generated", count=len(stories))
        except Exception as e:
            self.logger.error("generate_job_failed", error=str(e))

    async def _upload_videos_job(self):
        """Job: Upload generated videos"""
        try:
            count = self.service.upload_pending_videos()
            self.logger.info("videos_uploaded", count=count)
        except YouTubeQuotaExceeded as e:
            self.logger.warning("quota_exceeded", error=str(e))
        except Exception as e:
            self.logger.error("upload_job_failed", error=str(e))

    def start(self):
        """Start scheduler"""
        self.scheduler.start()
        self.logger.info("scheduler_started")

    def stop(self):
        """Stop scheduler"""
        self.scheduler.shutdown()
        self.logger.info("scheduler_stopped")
```

### ✅ Criterios de Éxito (Fase 4)

- [ ] OAuth flow funcionando (tokens se refrescan automáticamente)
- [ ] Quota tracking previene excepciones de API
- [ ] Scheduler ejecuta jobs en horarios correctos
- [ ] Logs estructurados de cada job

---

## 🔬 Fase 5: Testing & CI/CD (1 semana)

### Objetivos de Aprendizaje

- Pirámide de testing (unit → integration → e2e)
- GitHub Actions CI/CD
- Code coverage meaningful
- Testing best practices

### Implementación Práctica

#### Paso 1: Testing Strategy

```python
# tests/conftest.py
import pytest
from pathlib import Path
from redishort.domain.repositories import StoryRepository, VideoRepository
from redishort.core.services import VideoGenerationService

@pytest.fixture
def temp_db(tmp_path):
    """
    Aprende: pytest fixtures
    - tmp_path es un dir temporal que se limpia automáticamente
    - Útil para tests que necesitan filesystem
    """
    return tmp_path / "test.db"

@pytest.fixture
def story_repo(temp_db):
    """Fixture: StoryRepository con DB temporal"""
    from redishort.adapters.sqlite_repository import SQLiteStoryRepository
    return SQLiteStoryRepository(str(temp_db))

@pytest.fixture
def video_service(story_repo):
    """Fixture: VideoGenerationService con dependencias fake"""
    return VideoGenerationService(
        story_repo=story_repo,
        video_repo=FakeVideoRepository(),
        content_fetcher=FakeContentFetcher(),
        script_generator=FakeScriptGenerator(),
        video_renderer=FakeVideoRenderer(),
        video_uploader=FakeVideoUploader(),
    )


# tests/unit/test_domain_models.py
def test_reddit_story_is_suitable_for_video():
    """Test business logic in domain models"""
    story = RedditStory(
        id="test",
        title="Short",  # Too short
        selftext="Content",
        author="author",
        score=10,  # Too low
        created_utc=datetime.utcnow(),
        permalink="/r/test/1"
    )

    assert not story.is_suitable_for_video()


# tests/integration/test_sqlite_repository.py
@pytest.mark.integration
def test_sqlite_repository_round_trip(story_repo):
    """Test real database operations"""
    story = RedditStory(...)

    story_repo.save(story)
    retrieved = story_repo.get_by_id(story.id)

    assert retrieved == story


# tests/e2e/test_full_pipeline.py
@pytest.mark.e2e
@pytest.mark.slow
async def test_full_video_generation_pipeline(video_service):
    """
    End-to-end test: Story → Script → Video → Upload

    Aprende: E2E tests
    - Más lentos pero más realistas
    - Tocan todas las capas
    - Marcar como @pytest.mark.slow
    """
    # Fetch stories
    count = video_service.process_new_stories("askreddit")
    assert count > 0

    # Generate video
    stories = video_service.story_repo.get_unprocessed_stories(limit=1)
    video = await video_service.generate_video_from_story(stories[0].id)

    assert video.status == VideoStatus.GENERATED
    assert Path(video.video_path).exists()
```

#### Paso 2: GitHub Actions CI/CD

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        echo "$HOME/.local/bin" >> $GITHUB_PATH

    - name: Install dependencies
      run: poetry install

    - name: Run linter (ruff)
      run: poetry run ruff check src/

    - name: Run type checker (mypy)
      run: poetry run mypy src/

    - name: Run unit tests
      run: poetry run pytest tests/unit -v --cov=src --cov-report=xml

    - name: Run integration tests
      run: poetry run pytest tests/integration -v -m integration
      env:
        # Use test credentials
        REDDIT_CLIENT_ID: ${{ secrets.TEST_REDDIT_CLIENT_ID }}

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build-docker:
    runs-on: ubuntu-latest
    needs: test

    steps:
    - uses: actions/checkout@v3

    - name: Build Docker image
      run: docker build -t redishort:${{ github.sha }} .

    - name: Test Docker image
      run: |
        docker run redishort:${{ github.sha }} poetry run pytest tests/unit
```

**Aprende**:
- CI ejecuta en cada push/PR
- Falla rápido si algo no pasa
- Coverage automático
- Docker build garantiza reproducibilidad

### ✅ Criterios de Éxito (Fase 5)

- [ ] >80% code coverage (meaningful)
- [ ] CI passing en GitHub
- [ ] Pre-commit hooks instalados
- [ ] E2E test completo pasando

---

## 🚀 Fase 6: Production-Ready (1 semana)

### Objetivos de Aprendizaje

- Observability (metrics, tracing)
- Deployment con Docker
- Secrets management seguro
- Error alerting

### Implementación Práctica

#### Paso 1: Prometheus Metrics

```python
# src/redishort/observability/metrics.py
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import structlog

logger = structlog.get_logger()

# Metrics
stories_fetched = Counter('stories_fetched_total', 'Total stories fetched from Reddit')
videos_generated = Counter('videos_generated_total', 'Total videos generated', ['status'])
video_generation_duration = Histogram('video_generation_seconds', 'Time to generate video')
youtube_quota_used = Gauge('youtube_quota_used', 'YouTube API quota used today')

def start_metrics_server(port: int = 9090):
    """
    Aprende: Prometheus metrics
    - Expone /metrics endpoint
    - Prometheus lo scrapea automáticamente
    - Visualizable en Grafana
    """
    start_http_server(port)
    logger.info("metrics_server_started", port=port)


# Usage in service:
class VideoGenerationService:
    def process_new_stories(self, subreddit: str) -> int:
        stories = self.content_fetcher.fetch_stories(subreddit, limit=10)
        stories_fetched.inc(len(stories))  # Increment metric
        ...
```

#### Paso 2: Production Dockerfile

```dockerfile
# Multi-stage build
FROM python:3.11-slim as builder

WORKDIR /app

# Install Poetry
RUN pip install poetry==1.7.1

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies (no dev dependencies)
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-interaction --no-ansi

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for video processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy application code
COPY src/ ./src/
COPY assets/ ./assets/

# Create non-root user (security best practice)
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# Environment
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Run application
CMD ["python", "-m", "redishort.main"]
```

**Aprende**:
- Multi-stage build → imagen más pequeña (2GB → 500MB)
- Non-root user → seguridad
- Health check → Kubernetes sabe si está sano

#### Paso 3: docker-compose.yml para desarrollo

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - ENVIRONMENT=development
      - LOG_LEVEL=DEBUG
    env_file:
      - .env
    volumes:
      - ./src:/app/src  # Hot reload en desarrollo
      - ./data:/app/data
      - ./output:/app/output
    ports:
      - "9090:9090"  # Prometheus metrics
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: redishort
      POSTGRES_USER: redishort
      POSTGRES_PASSWORD: redishort
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9091:9090"

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

volumes:
  postgres_data:
```

### ✅ Criterios de Éxito (Fase 6)

- [ ] Metrics expuestos en /metrics
- [ ] Docker compose up funciona end-to-end
- [ ] Logs estructurados (parseables)
- [ ] Secrets en variables de entorno (no hardcoded)
- [ ] Health checks pasando

---

## 📊 Resumen del Roadmap

| Fase | Duración | Enfoque | Entregables |
|------|----------|---------|-------------|
| 0 | 1 sem | Setup & Tooling | Poetry, ruff, mypy, structlog, pre-commit |
| 1 | 2 sem | Core Architecture | Domain models, repositories, services, DI, tests |
| 2 | 1.5 sem | External Adapters | Reddit, Gemini, retry logic, circuit breaker |
| 3 | 2 sem | Video Pipeline | TTS, video composition, async pipeline |
| 4 | 1 sem | YouTube & Scheduler | OAuth, quota, APScheduler |
| 5 | 1 sem | Testing & CI/CD | Unit/int/e2e tests, GitHub Actions, coverage |
| 6 | 1 sem | Production | Metrics, Docker, observability |
| **Total** | **8.5 semanas** | | **Sistema production-ready** |

---

## 🎯 Conceptos Clave Aprendidos

Al completar este roadmap, habrás dominado:

### Arquitectura
- ✅ Clean Architecture / Hexagonal Architecture
- ✅ Domain-Driven Design (DDD)
- ✅ SOLID principles
- ✅ Dependency Injection
- ✅ Repository pattern
- ✅ Service layer pattern

### Resiliencia
- ✅ Retry with exponential backoff
- ✅ Circuit breaker
- ✅ Rate limiting
- ✅ Graceful degradation

### Testing
- ✅ Unit tests (fakes > mocks)
- ✅ Integration tests
- ✅ E2E tests
- ✅ Test pyramid
- ✅ >80% meaningful coverage

### DevOps
- ✅ Docker multi-stage builds
- ✅ CI/CD con GitHub Actions
- ✅ Observability (logs, metrics, tracing)
- ✅ Secrets management

### Python Moderno
- ✅ Type hints + mypy
- ✅ Dataclasses
- ✅ Context managers
- ✅ Async/await
- ✅ Protocols (duck typing tipado)

---

## 📚 Recursos Recomendados

### Libros
1. **Architecture Patterns with Python** (Cosmic Python) - GRATIS online
2. **Clean Architecture** - Robert C. Martin
3. **Release It!** - Michael Nygard (resiliencia)
4. **Python Testing with pytest** - Brian Okken

### Cursos
1. [ArjanCodes YouTube Channel](https://www.youtube.com/@ArjanCodes) - Clean code en Python
2. [mCoding YouTube Channel](https://www.youtube.com/@mCoding) - Python avanzado
3. [Real Python](https://realpython.com/) - Tutoriales de calidad

### Comunidades
- r/Python
- Python Discord
- Stack Overflow

---

## 🏁 Siguientes Pasos

1. **Crea un nuevo repo**: `redishort-v2`
2. **Empieza por Fase 0**: No saltes pasos
3. **Documenta tu aprendizaje**: README.md con TIL (Today I Learned)
4. **Haz commits pequeños**: Cada concepto = 1 commit
5. **Pide feedback**: Code review de amigos/comunidad

---

## ✨ Filosofía Final

> "El código no es el producto final, el aprendizaje sí lo es."

No te apresures. Cada fase está diseñada para enseñarte algo fundamental. Si algo no tiene sentido, investiga más antes de continuar.

Al final de este roadmap, no solo tendrás un sistema production-ready, sino que **entenderás profundamente cómo construir software de calidad profesional**.

¡Buena suerte! 🚀

# Food Ordering System

A modern, full-stack food ordering application built with FastAPI, React, and PostgreSQL. This enterprise-grade system features comprehensive observability, containerization, and Kubernetes deployment capabilities.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  React Frontend │    │  FastAPI Backend│    │   PostgreSQL    │
│     (Vite)      │◄──►│   (Python)      │◄──►│    Database     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         └──────────────►│  Observability  │◄─────────────┘
                         │ (OTEL/Grafana)  │
                         └─────────────────┘
```

## 🚀 Features

- **Modern React Frontend**: Built with React 19, TypeScript, and Vite
- **FastAPI Backend**: High-performance Python API with automatic OpenAPI documentation
- **PostgreSQL Database**: Robust relational database with comprehensive schema
- **Full Observability**: OpenTelemetry integration with Grafana, Prometheus, and Zipkin
- **Containerization**: Complete Docker Compose setup for development
- **Kubernetes Ready**: Production-ready Kubernetes manifests
- **Testing**: Comprehensive test suite with pytest and integration tests
- **CI/CD Ready**: GitHub Actions workflows for automated testing and deployment

## 🛠️ Tech Stack

### Frontend
- **React 19** with TypeScript
- **Vite** for blazing-fast development
- **React Bootstrap** for responsive UI components
- **React Query** for efficient data fetching
- **Axios** for HTTP client
- **React Router** for navigation

### Backend
- **FastAPI** for high-performance API development
- **SQLAlchemy** for database ORM
- **Pydantic** for data validation
- **asyncpg** for async PostgreSQL connection
- **OpenTelemetry** for observability
- **pytest** for testing

### Infrastructure
- **PostgreSQL** for data persistence
- **Docker & Docker Compose** for containerization
- **Kubernetes** for orchestration
- **Grafana** for monitoring dashboards
- **Prometheus** for metrics collection
- **Zipkin** for distributed tracing
- **Loki** for log aggregation

## 🚦 Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 20+ (for local development)
- Python 3.12+ (for local development)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jesus-sunuc/FoodOrdering.git
   cd FoodOrdering
   ```

2. **Start the application with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Local Development

#### Frontend Development
```bash
cd client
npm install
npm run dev
```

#### Backend Development
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

### Production Build
```bash
cd client
npm run build
```

## 📊 Observability

The application includes comprehensive observability features:

- **Metrics**: Custom metrics collection with OpenTelemetry
- **Tracing**: Distributed tracing across all services
- **Logging**: Structured logging with correlation IDs
- **Dashboards**: Pre-configured Grafana dashboards

Access monitoring tools:
- Grafana: http://localhost:3001
- Prometheus: http://localhost:9090
- Zipkin: http://localhost:9411

## 🧪 Testing

### Backend Tests
```bash
cd api
pytest
```

### Integration Tests
```bash
cd api
python integration_test.py
```

## 🚀 Deployment

### Kubernetes Deployment

1. **Apply Kubernetes manifests**
   ```bash
   kubectl apply -f kube/
   ```

2. **Verify deployment**
   ```bash
   kubectl get pods
   kubectl get services
   ```

### Environment Configuration

Create environment files for different deployments:

**API Environment (.env)**
```env
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
DEBUG=false
```

## 📁 Project Structure

```
FoodOrdering/
├── api/                    # FastAPI backend
│   ├── features/          # Feature-based modules
│   │   └── item/         # Item management
│   ├── models/           # Pydantic models
│   ├── routes/           # API routes
│   ├── services/         # Business logic
│   └── main.py          # Application entry point
├── client/               # React frontend
│   ├── src/
│   │   ├── components/   # Reusable UI components
│   │   ├── features/     # Feature-based modules
│   │   └── utils/        # Utility functions
│   └── package.json
├── kube/                 # Kubernetes manifests
├── configs/              # Configuration files
├── docker-compose.yml    # Development orchestration
└── init.sql             # Database initialization
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for TypeScript/React code
- Write tests for new features
- Update documentation as needed

## 📄 API Documentation

The API documentation is automatically generated and available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Related Projects

- [MAUI Mobile App](https://github.com/Zane-Clegg/FastFoodAppPrototyping) - Cross-platform mobile application

## 👥 Team

Developed as part of Fall 2024 coursework with focus on modern software engineering practices and enterprise architecture patterns.

## 🆘 Support

For support and questions:
- Open an issue on GitHub
- Check the API documentation
- Review the monitoring dashboards for system health

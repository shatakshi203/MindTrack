# 🧠 MindTrack - University Mental Health Platform

## 📋 Project Overview
MindTrack is a comprehensive mental health support platform designed for university students. It provides easy access to therapy sessions, mental health assessments, AI-powered chatbot support, and real-time analysis to help students maintain their mental well-being.

## ✨ Features
- 🔐 **Secure Authentication** - Gmail OTP verification
- 📝 **Mental Health Assessment** - Comprehensive Q&A questionnaire (PHQ-9, GAD-7)
- 📅 **Therapy Booking System** - Easy appointment scheduling with therapists
- 🤖 **AI Chatbot** - 24/7 mental health support and conversation
- 📊 **AI/ML Analysis** - Real-time problem analysis and insights
- 👨‍⚕️ **Therapist Dashboard** - Manage appointments and patient insights
- 📱 **Responsive Design** - Works seamlessly on all devices
- 🚨 **Emergency Support** - Crisis intervention and immediate help
- 📈 **Progress Tracking** - Monitor mental health journey over time

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python 3.8+)
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **AI/ML:** scikit-learn, transformers, nltk
- **Authentication:** JWT with Gmail OTP verification
- **Email Service:** SMTP with Gmail integration
- **Styling:** Modern CSS with animations and card layouts

## 🚀 Quick Start

### Automated Setup (Recommended)
```bash
# Run the automated setup script
python setup.py
```

### Manual Setup

#### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Git
- Gmail account for email services

#### Installation Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd MindTrack
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r backend/requirements.txt
```

4. **Setup PostgreSQL Database**
```sql
-- Connect to PostgreSQL and create database
CREATE DATABASE mindtrack;

-- Run the schema file
\i database/schema.sql
```

5. **Configure Environment**
```bash
# Copy environment template
cp backend/.env.example backend/.env

# Edit backend/.env with your settings:
# - DATABASE_URL
# - EMAIL_ADDRESS and EMAIL_PASSWORD
# - SECRET_KEY
```

6. **Run the application**
```bash
cd backend
python main.py
```

7. **Access the platform**
Open your browser to: `http://localhost:8000`

## 📁 Project Structure
```
MindTrack/
├── backend/                    # FastAPI backend application
│   ├── app/
│   │   ├── models/            # Database models
│   │   │   ├── user.py        # User and therapist models
│   │   │   ├── assessment.py  # Assessment and chat models
│   │   │   └── booking.py     # Appointment models
│   │   ├── routes/            # API endpoints
│   │   │   ├── auth.py        # Authentication routes
│   │   │   ├── assessment.py  # Mental health assessments
│   │   │   ├── booking.py     # Appointment booking
│   │   │   ├── chatbot.py     # AI chatbot functionality
│   │   │   └── admin.py       # Admin dashboard
│   │   ├── services/          # Business logic
│   │   │   ├── auth_service.py    # Authentication logic
│   │   │   ├── email_service.py   # Email functionality
│   │   │   └── ai_service.py      # AI/ML services
│   │   └── database.py        # Database configuration
│   ├── requirements.txt       # Python dependencies
│   ├── main.py               # Application entry point
│   └── .env.example          # Environment template
├── frontend/                  # Frontend application
│   ├── templates/            # HTML templates
│   │   ├── index.html        # Landing page
│   │   └── dashboard.html    # User dashboard
│   └── static/               # Static assets
│       ├── css/              # Stylesheets
│       │   ├── style.css     # Main styles
│       │   └── dashboard.css # Dashboard styles
│       └── js/               # JavaScript files
│           ├── main.js       # Main functionality
│           └── dashboard.js  # Dashboard logic
├── database/
│   └── schema.sql            # Database schema and sample data
├── setup.py                  # Automated setup script
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables
Create `backend/.env` file with the following variables:

```env
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/mindtrack

# Security
SECRET_KEY=your-super-secret-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email (Gmail SMTP)
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# Application
DEBUG=True
```

### Gmail Setup for OTP
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this password in EMAIL_PASSWORD

## 🎯 Core Features

### 1. User Authentication
- **Registration**: Students register with university email
- **OTP Verification**: Secure email-based verification
- **JWT Tokens**: Stateless authentication
- **Session Management**: Secure login/logout

### 2. Mental Health Assessments
- **PHQ-9**: Depression screening questionnaire
- **GAD-7**: Anxiety assessment tool
- **Custom Assessments**: Extensible question framework
- **AI Analysis**: Automated insights and recommendations
- **Progress Tracking**: Historical assessment data

### 3. Therapy Booking System
- **Therapist Profiles**: Licensed professionals with specializations
- **Availability Management**: Real-time scheduling
- **Appointment Types**: Individual, group, emergency sessions
- **Email Confirmations**: Automated booking confirmations
- **Rating System**: Post-session feedback

### 4. AI Chatbot
- **24/7 Support**: Always available mental health assistance
- **Sentiment Analysis**: Real-time emotion detection
- **Crisis Detection**: Automatic identification of emergency situations
- **Conversation History**: Persistent chat sessions
- **Personalized Responses**: Context-aware AI interactions

### 5. Emergency Support
- **Crisis Hotlines**: Direct links to emergency services
- **Immediate Help**: Connect with available therapists
- **Emergency Requests**: Priority support system
- **Safety Resources**: Crisis intervention tools

## 🤖 AI/ML Features

### Sentiment Analysis
- Real-time emotion detection in chat messages
- Mood tracking over time
- Pattern recognition in user behavior

### Assessment Analysis
- Automated scoring of mental health questionnaires
- Risk level calculation
- Personalized recommendations
- Trend analysis

### Crisis Detection
- Keyword-based crisis identification
- Automatic escalation protocols
- Emergency response triggers

## 👥 User Roles

### Students
- Take mental health assessments
- Book therapy appointments
- Chat with AI support
- Track progress over time
- Access emergency resources

### Therapists
- Manage availability and appointments
- View patient assessment results
- Access session notes and history
- Handle emergency requests

### Administrators
- User and therapist management
- System analytics and reporting
- Emergency request oversight
- Platform configuration

## 📊 Database Schema

### Key Tables
- **users**: Student information and authentication
- **therapists**: Licensed mental health professionals
- **mental_health_assessments**: Assessment responses and scores
- **appointments**: Therapy session bookings
- **chat_sessions**: AI chatbot conversations
- **emergency_requests**: Crisis support requests

## 🔒 Security Features

### Data Protection
- **Encryption**: All sensitive data encrypted at rest
- **HTTPS**: Secure data transmission
- **Input Validation**: SQL injection prevention
- **Rate Limiting**: API abuse protection

### Privacy Compliance
- **HIPAA Considerations**: Healthcare data protection
- **Data Anonymization**: Optional anonymous usage
- **Consent Management**: Clear privacy policies
- **Data Retention**: Configurable data lifecycle

## 🧪 Testing

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
python -m pytest

# Run with coverage
python -m pytest --cov=app
```

### Test Coverage
- Unit tests for all API endpoints
- Integration tests for database operations
- Frontend functionality testing
- AI service validation

## 📈 Monitoring and Analytics

### Application Metrics
- User registration and engagement
- Assessment completion rates
- Appointment booking statistics
- Chat session analytics

### Mental Health Insights
- Severity level distributions
- Trend analysis over time
- Crisis intervention metrics
- Treatment outcome tracking

## 🚀 Deployment

### Development
```bash
# Start development server
cd backend
python main.py
```

### Production Considerations
- **Database**: Use managed PostgreSQL service
- **Email**: Configure production SMTP settings
- **Security**: Update SECRET_KEY and enable HTTPS
- **Monitoring**: Implement logging and error tracking
- **Backup**: Regular database backups

## 🎯 Project Goals
This project is developed as part of BTech CSE final year major project, focusing on:
- Mental health awareness in educational institutions
- Technology-driven healthcare solutions
- AI/ML applications in healthcare
- Full-stack web development
- Real-world problem solving

## 👥 Target Users
- **Primary**: University students seeking mental health support
- **Secondary**: Therapists and counselors
- **Tertiary**: University administration and mental health researchers

## 🔮 Future Enhancements

### Short-term
- Mobile app development (React Native/Flutter)
- Advanced AI models for better sentiment analysis
- Group therapy session support
- Integration with university student information systems

### Long-term
- Predictive analytics for mental health trends
- VR/AR therapy sessions
- Peer support networks
- Research data anonymization and sharing
- Multi-language support

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Standards
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for all functions
- Maintain test coverage above 80%

## 📄 License
This project is developed for educational purposes as part of a BTech CSE final year project.

## 🆘 Support

### Getting Help
- Check the troubleshooting section below
- Review the error logs in `logs/` directory
- Ensure all dependencies are properly installed
- Verify database connection and configuration

### Troubleshooting

#### Common Issues

**Database Connection Error**
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Verify database exists
psql -l | grep mindtrack

# Test connection
psql -d mindtrack -c "SELECT 1;"
```

**Email OTP Not Working**
- Verify Gmail App Password is correct
- Check EMAIL_ADDRESS and EMAIL_PASSWORD in .env
- Ensure 2-factor authentication is enabled on Gmail
- Check spam folder for OTP emails

**Import Errors**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r backend/requirements.txt
```

**Port Already in Use**
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process or use different port
python main.py --port 8001
```

### Contact Information
For technical support or questions about this project, please refer to the project documentation or create an issue in the repository.

---
**Developed with ❤️ for university mental health support**

*"Mental health is not a destination, but a process. It's about how you drive, not where you're going."* - Noam Shpancer

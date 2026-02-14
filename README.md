🎓 SkillSwap

A peer-to-peer learning platform where students teach, learn, and collaborate through video lessons and direct chat.

SkillSwap is a full-stack Django web application that enables students to share knowledge by uploading video-based skills and interact through a built-in messaging system.

📌 **Overview**

SkillSwap allows users to:

 **👨‍Teach by uploading skill-based video lessons

**📖 Learn by browsing available topics

**💬 Communicate directly with teachers via chat

**🔐 Securely authenticate and manage accounts

The platform promotes collaborative learning within a student community.

**✨ **Features****

🔐 Authentication System

  * User Registration

  * Login & Logout

  * Secure session management

 * Role-based interface (Teacher / Student)

📚 **Skill Management**

* Create a new skill post

* Upload video lessons (MP4 supported)

* Add skill description

* Edit existing skills (teacher only)

* View detailed skill pages

**💬 **Chat System****

* One-to-one messaging between student and teacher

* Timestamped messages

* Clean, responsive UI

* Conditional UI rendering (sender/receiver styling)

🎥 **Media Handling**

* Video upload via Django FileField

* Integrated HTML5 video player

* Secure media configuration

**🛠️ Tech Stack**

Layer     |  	   Technology

Backend      |	Django (Python)

Frontend    |	HTML5, CSS3

Database	 |   SQLite (default)

AuthSystem	  |  Django Authentication

Media	     |    Django File Upload





**🔒 **Access Control Logic****

 * Only authenticated users can access skill pages.

* Only the teacher who created a skill can edit it.

* Students can message the teacher.

* Teachers cannot message themselves.

🎯 ****Learning Outcomes****

This project demonstrates:

* Django project architecture

* Model-View-Template (MVT) pattern

* User authentication & authorization

* File/media handling

* Dynamic template rendering

* UI/UX structuring with CSS

**🚀 **Future Improvements****

* WebSocket-based real-time chat (Django Channels)

* Search & filtering functionality

* User profile pages

* Skill ratings & reviews

* Email notifications

* Deployment (Render / AWS / Heroku)

* REST API integration

🧪 ****Possible Enhancements for Production****

* PostgreSQL integration

* Cloud media storage (AWS S3)

* Environment variable management

* Docker support

* Unit & integration testing

*CI/ CD pipeline

****👨‍💻 Author****

Developed as a full-stack Django academic project to showcase backend development, authentication systems, and interactive web design.

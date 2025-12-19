# PeerLearn Frontend

Modern React frontend for the PeerLearn study companion platform.

## 🚀 Quick Start

### Prerequisites
- Node.js 16+
- npm or yarn

### Installation

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm start
```

4. **Open in browser**
```
http://localhost:3000
```

## 📁 Project Structure

```
frontend/
├── public/
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── ProtectedRoute.js
│   │   ├── LoadingSpinner.js
│   │   ├── Layout.js
│   │   ├── CreateClassroomModal.js
│   │   ├── JoinClassroomModal.js
│   │   ├── CreateRoomModal.js
│   │   └── ChatInterface.js
│   ├── pages/
│   │   ├── LoginPage.js
│   │   ├── RegisterPage.js
│   │   ├── DashboardPage.js
│   │   ├── ClassroomPage.js
│   │   ├── FriendsPage.js
│   │   └── ProfilePage.js
│   ├── contexts/
│   │   ├── AuthContext.js
│   │   └── SocketContext.js
│   ├── utils/
│   │   └── api.js
│   ├── App.js
│   ├── index.js
│   └── index.css
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

## 🎨 UI/UX Features

### Design System
- **Modern & Minimalistic**: Clean, professional interface
- **Responsive Design**: Mobile-friendly across all devices
- **Dark/Light Theme**: Consistent color scheme
- **Smooth Animations**: Framer Motion for delightful interactions
- **Accessibility**: WCAG compliant components

### Color Palette
- **Primary**: Blue gradient (#6366f1 to #764ba2)
- **Secondary**: Purple accents
- **Success**: Green (#22c55e)
- **Warning**: Yellow (#f59e0b)
- **Error**: Red (#ef4444)
- **Neutral**: Gray scale

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: Bold, clear hierarchy
- **Body**: Readable, comfortable line height
- **Code**: Monospace for technical content

## 🧩 Components

### Core Components

#### `Layout.js`
- Main application layout with sidebar navigation
- Responsive mobile menu
- User profile display
- Connection status indicator

#### `ProtectedRoute.js`
- Route protection for authenticated users
- Loading states during authentication check
- Redirect to login for unauthenticated users

#### `LoadingSpinner.js`
- Reusable loading indicator
- Multiple sizes (sm, md, lg, xl)
- Consistent styling across app

### Modal Components

#### `CreateClassroomModal.js`
- Classroom creation form
- AI-powered name suggestions
- Form validation and error handling

#### `JoinClassroomModal.js`
- Join classroom with invite code
- Input validation
- Success/error feedback

#### `CreateRoomModal.js`
- Room creation within classrooms
- Subject-based room suggestions
- Admin-only access control

### Chat Components

#### `ChatInterface.js`
- Real-time messaging interface
- Message editing and deletion
- AI chat summarization
- WebSocket integration
- Message moderation

## 📱 Pages

### Authentication Pages

#### `LoginPage.js`
- Email/password login form
- Google OAuth integration (ready)
- Password visibility toggle
- Form validation
- Responsive design

#### `RegisterPage.js`
- Multi-step registration process
- Email verification flow
- Profile completion
- Study interests management
- Form validation

### Main Application Pages

#### `DashboardPage.js`
- User statistics display
- Classroom grid view
- Quick actions (create/join)
- Search functionality
- Responsive cards

#### `ClassroomPage.js`
- Room navigation sidebar
- Chat interface integration
- Admin controls
- Member management
- Real-time updates

#### `FriendsPage.js`
- Friends list display
- Friend request management
- User search functionality
- Add/remove friends
- Request status tracking

#### `ProfilePage.js`
- Profile information display
- Editable profile fields
- Study interests management
- Avatar upload (ready)
- Statistics display

## 🔧 State Management

### React Context

#### `AuthContext.js`
- User authentication state
- Login/logout functionality
- Profile management
- Token handling
- Error management

#### `SocketContext.js`
- WebSocket connection management
- Real-time event handling
- Room joining/leaving
- Message broadcasting
- Connection status

### React Query
- Server state management
- Caching and synchronization
- Background updates
- Error handling
- Loading states

## 🌐 API Integration

### API Client (`utils/api.js`)
- Axios-based HTTP client
- Automatic token handling
- Request/response interceptors
- Error handling
- Token refresh logic

### API Endpoints
- **Authentication**: Login, register, profile management
- **Friends**: Search, requests, management
- **Classrooms**: CRUD operations, room management
- **Chat**: Messages, real-time communication

## 🎭 Animations

### Framer Motion
- Page transitions
- Component animations
- Loading states
- Hover effects
- Modal animations

### Animation Types
- **Fade In**: Smooth opacity transitions
- **Slide Up**: Content appearing from bottom
- **Scale**: Modal and card animations
- **Stagger**: List item animations

## 📱 Responsive Design

### Breakpoints
- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

### Mobile Features
- Collapsible sidebar
- Touch-friendly buttons
- Swipe gestures
- Mobile-optimized forms
- Responsive images

## 🎨 Styling

### Tailwind CSS
- Utility-first CSS framework
- Custom color palette
- Responsive utilities
- Component classes
- Dark mode support

### Custom Classes
```css
.btn-primary    /* Primary button styling */
.btn-secondary  /* Secondary button styling */
.btn-outline    /* Outline button styling */
.card           /* Card container */
.input          /* Form input styling */
.badge-*        /* Status badges */
```

## 🔐 Security

### Authentication
- JWT token management
- Automatic token refresh
- Secure token storage
- Route protection
- Session management

### Data Protection
- Input sanitization
- XSS prevention
- CSRF protection
- Secure API calls
- Error handling

## 🚀 Performance

### Optimization
- Code splitting
- Lazy loading
- Image optimization
- Bundle optimization
- Caching strategies

### Loading States
- Skeleton screens
- Loading spinners
- Progressive loading
- Error boundaries
- Fallback components

## 🧪 Testing

### Testing Setup
```bash
# Install testing dependencies
npm install --save-dev @testing-library/react @testing-library/jest-dom

# Run tests
npm test

# Run tests with coverage
npm test -- --coverage
```

### Test Types
- Unit tests for components
- Integration tests for pages
- API integration tests
- User interaction tests

## 📦 Build & Deployment

### Development
```bash
npm start          # Start development server
npm run build      # Build for production
npm test           # Run tests
npm run eject      # Eject from Create React App
```

### Production Build
```bash
npm run build
# Creates optimized build in 'build' directory
```

### Environment Variables
```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_GOOGLE_CLIENT_ID=your-google-client-id
```

## 🔧 Configuration

### Tailwind Config
- Custom color palette
- Font family settings
- Animation keyframes
- Component utilities
- Responsive breakpoints

### Package.json Scripts
- `start`: Development server
- `build`: Production build
- `test`: Run tests
- `eject`: Eject from CRA

## 🎯 Features

### Real-time Features
- Live chat messaging
- Online status indicators
- Real-time notifications
- Instant updates
- WebSocket integration

### User Experience
- Intuitive navigation
- Smooth transitions
- Loading states
- Error handling
- Success feedback

### Accessibility
- Keyboard navigation
- Screen reader support
- High contrast mode
- Focus management
- ARIA labels

## 🚀 Deployment

### Static Hosting
- **Vercel**: `vercel --prod`
- **Netlify**: Connect GitHub repository
- **AWS S3**: Upload build folder
- **GitHub Pages**: Use gh-pages package

### Environment Setup
1. Set production API URL
2. Configure Google OAuth
3. Set up domain
4. Enable HTTPS
5. Configure CDN

## 🐛 Debugging

### Development Tools
- React Developer Tools
- Redux DevTools
- Network tab
- Console logging
- Error boundaries

### Common Issues
1. **CORS Errors**: Check API configuration
2. **Token Issues**: Verify authentication flow
3. **WebSocket Errors**: Check connection settings
4. **Build Errors**: Clear cache and reinstall

## 🤝 Contributing

### Development Workflow
1. Fork repository
2. Create feature branch
3. Make changes
4. Add tests
5. Submit pull request

### Code Style
- ESLint configuration
- Prettier formatting
- Component structure
- Naming conventions
- Documentation

## 📄 License

MIT License - see LICENSE file for details.

## 🆘 Support

### Getting Help
- Check documentation
- Review code comments
- Create GitHub issue
- Check API documentation
- Review error messages

### Common Solutions
- Clear browser cache
- Restart development server
- Check network connectivity
- Verify environment variables
- Update dependencies




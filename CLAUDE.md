# AI-Powered Advisor Dashboard System

## Project Background

This is a comprehensive AI-powered advisor dashboard system built for Capital Group that demonstrates personalized content delivery for financial advisors. The system uses LLM/AI technology to intelligently parse user prompts and match relevant articles from a curated corpus, providing a dynamic and personalized experience for different advisor users.

## Core Features

### 1. Dual-User Authentication System
- **Nat (LPL Financial)**: Username: `nat`, Password: `capital123`
- **K (Edward Jones)**: Username: `k`, Password: `advisor456`
- Session management via localStorage
- Automatic user detection and personalized content loading

### 2. AI-Powered Content Matching
- **LLM Integration**: Uses OpenAI GPT API for semantic text parsing
- **Intelligent Parsing**: Recognizes firm shortforms (EJ=Edward Jones, MS=Morgan Stanley, RJ=Raymond James, etc.)
- **Article Matching**: Matches user prompts against full article corpus based on tickers and content relevance
- **Fallback System**: Rule-based parsing when LLM is unavailable

### 3. Dynamic Content Management
- **Default State**: Shows 8 practice management articles initially (clean demo state)
- **Personalized State**: Updates to show relevant content after prompt submission
- **Real-time Updates**: Cross-browser window synchronization via localStorage
- **Grid Position Mapping**: Each tile position always uses the same image (1-8) regardless of content

### 4. Professional UI/UX
- **Capital Group Branding**: Official logo and color scheme
- **Responsive Design**: CSS Grid layout with proper flexbox alignment
- **Image Management**: Local image assets (image1.png through image8.png)
- **Consistent Styling**: Professional card-based layout with proper typography

## File Structure

### Main Files
- **`dist/index.html`**: Main dashboard application with complete functionality
- **`prompt_console.html`**: AI-powered prompt processing system
- **`articles.json`**: Clean default articles (8 practice management articles only)
- **`articles_full_backup.json`**: Complete article corpus including ticker-specific content
- **`images/`**: Local image assets (image1.png through image8.png)
- **`capital_group_logo.png`**: Official Capital Group logo

### Key Components

#### Authentication System
```javascript
const credentials = {
    nat: { password: "capital123", displayName: "Nat", chip: "Nat Bala", advisorId: "nat", firm: "LPL Financial" },
    k: { password: "advisor456", displayName: "K", chip: "K", advisorId: "k", firm: "Edward Jones" }
};
```

#### Image Mapping Logic
```javascript
const gridPositionImages = [
    'images/image1.png', // Grid position 1 (top-left)
    'images/image2.png', // Grid position 2 (top-second)
    'images/image3.png', // Grid position 3 (top-third)
    'images/image4.png', // Grid position 4 (top-right)
    'images/image5.png', // Grid position 5 (bottom-left)
    'images/image6.png', // Grid position 6 (bottom-second)
    'images/image7.png', // Grid position 7 (bottom-third)
    'images/image8.png'  // Grid position 8 (bottom-right)
];
```

## Technical Implementation

### CSS Architecture
- **CSS Variables**: Consistent color scheme using CSS custom properties
- **Flexbox Layout**: Proper content alignment with `feed-card-content` wrapper
- **Grid System**: 4-column responsive grid for article tiles
- **Navigation**: Horizontal navigation with `white-space: nowrap` for proper text display

### JavaScript Features
- **Local Storage Management**: Session persistence and feed synchronization
- **Dynamic Content Loading**: Real-time article injection and removal
- **Error Handling**: Graceful fallbacks for missing images and API failures
- **Cross-Window Communication**: Real-time updates across multiple browser instances

### AI Integration
- **Prompt Processing**: Semantic understanding of user requests
- **Entity Recognition**: Automatic detection of firms, tickers, and content themes
- **Confidence Scoring**: Article matching with relevance indicators
- **Shortform Recognition**: Intelligent expansion of common abbreviations

## Demo Flow

1. **Initial State**: Shows 8 static practice management articles
2. **User Login**: Authenticates and personalizes welcome message
3. **Prompt Submission**: User types request in prompt console
4. **AI Processing**: LLM analyzes request and matches relevant articles
5. **Content Update**: Dashboard updates with personalized article mix
6. **Cross-Session Sync**: Updates appear across all open browser windows

## URL Standardization

All article URLs point to `capitalgroup.com` domain:
- Practice management articles: `/advisor/practicelab/`
- Investment insights: `/advisor/insights/`
- Growth strategies: `/advisor/pro/pathways-to-growth/`
- Product information: `/advisor/investments/`

## Important Notes

### Image Management
- Images are stored locally in `images/` folder and copied to `dist/images/`
- Each grid position always uses the same image regardless of content changes
- This prevents image duplication issues during dynamic content updates

### Data Sources
- **Default Articles**: `articles.json` (practice management only)
- **Full Corpus**: `articles_full_backup.json` (includes ticker-specific content)
- **Prompt Processing**: Uses full corpus for AI matching

### Session Management
- User sessions persist across browser refreshes
- Feed data syncs across multiple browser windows
- "Clear All Feeds" functionality resets to default state

## Development Commands

To run the application:
```bash
# Open main dashboard
start dist/index.html

# Open prompt console (for testing AI integration)
start prompt_console.html
```

## Technical Debt and Future Enhancements

- Consider implementing proper API endpoints for article management
- Add more sophisticated caching mechanisms
- Implement user preference storage
- Add analytics tracking for article engagement
- Consider implementing real-time collaboration features

This system serves as a comprehensive demo of AI-powered content personalization in a financial services context, showcasing both technical sophistication and professional presentation quality.
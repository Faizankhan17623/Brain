---
title: "React Snippets"
date: 2026-04-27
type: resource
status: active
tags:
  - react
  - snippets
  - frontend
---

# React Snippets

---

## Hooks

### useState with object
```javascript
const [form, setForm] = useState({ name: '', email: '', password: '' });
const handleChange = (e) => setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));
```

### useEffect — fetch on mount
```javascript
useEffect(() => {
  let cancelled = false;
  const load = async () => {
    const data = await fetchData('/api/items');
    if (!cancelled) setItems(data);
  };
  load();
  return () => { cancelled = true; };
}, []);
```

### useEffect — cleanup event listener
```javascript
useEffect(() => {
  const handler = (e) => console.log(e.key);
  window.addEventListener('keydown', handler);
  return () => window.removeEventListener('keydown', handler);
}, []);
```

### useRef — focus input on mount
```javascript
const inputRef = useRef(null);
useEffect(() => { inputRef.current?.focus(); }, []);
// In JSX: <input ref={inputRef} />
```

### useContext — simple pattern
```javascript
// 1. Create
const ThemeContext = createContext('light');
// 2. Provide
<ThemeContext.Provider value="dark"><App /></ThemeContext.Provider>
// 3. Consume
const theme = useContext(ThemeContext);
```

### useMemo — expensive calculation
```javascript
const sortedList = useMemo(() => [...items].sort((a, b) => a.name.localeCompare(b.name)), [items]);
```

### useCallback — stable function reference
```javascript
const handleSubmit = useCallback(async (data) => {
  await api.post('/submit', data);
}, []); // deps array — add values used inside
```

### Custom hook — useDebounce
```javascript
const useDebounce = (value, delay = 300) => {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
};
```

### Custom hook — useFetch
```javascript
const useFetch = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData).catch(setError).finally(() => setLoading(false));
  }, [url]);
  return { data, loading, error };
};
```

---

## Patterns

### Protected Route
```javascript
const ProtectedRoute = ({ children }) => {
  const { user } = useAuth();
  return user ? children : <Navigate to="/login" replace />;
};
```

### Error Boundary (class component)
```javascript
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  render() {
    return this.state.hasError ? <h2>Something went wrong.</h2> : this.props.children;
  }
}
```

### Lazy load + Suspense
```javascript
const HeavyComponent = lazy(() => import('./HeavyComponent'));
// In render:
<Suspense fallback={<Spinner />}><HeavyComponent /></Suspense>
```

---

*Last updated: 2026-04-27 | Back to [[snippets/README]]*

const STATIC_CACHE = 'pwa-static-v1';
const DYNAMIC_CACHE = 'pwa-dynamic-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/offline.html'
];

// Cache statique à l'installation
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(cache => {
        console.log('[Service Worker] Caching static assets');
        return cache.addAll(urlsToCache);
      })
  );
});

// Nettoyage des anciens caches à l'activation
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames =>
      Promise.all(
        cacheNames
          .filter(name => name !== STATIC_CACHE && name !== DYNAMIC_CACHE)
          .map(name => caches.delete(name))
      )
    )
  );
});

// Intercepter les requêtes
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(res => {
        return caches.open(DYNAMIC_CACHE).then(cache => {
          // Mise en cache dynamique
          cache.put(event.request.url, res.clone());
          return res;
        });
      })
      .catch(() => {
        // Si fetch échoue (hors ligne), on regarde dans le cache
        return caches.match(event.request)
          .then(cachedResponse => {
            return cachedResponse || caches.match('/offline.html');
          });
      })
  );
});

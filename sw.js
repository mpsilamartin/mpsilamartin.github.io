const CACHE_NAME = 'pwa-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/offline.html'
];

// Installer le SW et mettre les fichiers en cache
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Fichiers mis en cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Activer le SW et nettoyer les anciens caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames =>
      Promise.all(
        cacheNames.map(name => {
          if (name !== CACHE_NAME) {
            console.log('Cache supprimé :', name);
            return caches.delete(name);
          }
        })
      )
    )
  );
});

// Intercepter les requêtes
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .catch(() => caches.match(event.request))
      .then(response => response || caches.match('/offline.html'))
  );
});

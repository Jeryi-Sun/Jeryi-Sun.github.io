(() => {
  const menus = Array.from(document.querySelectorAll('[data-mobile-menu]'));

  for (const menu of menus) {
    menu.addEventListener('toggle', () => {
      if (!menu.open) return;
      const links = menu.querySelector('.academic-home__mobile-links');
      if (!links) return;
      const available = window.innerHeight - links.getBoundingClientRect().top - 12;
      links.style.maxHeight = `${Math.max(44, available)}px`;
    });
  }

  window.addEventListener('resize', () => {
    for (const menu of menus) menu.open = false;
  });

  document.addEventListener('click', (event) => {
    if (!(event.target instanceof Element)) return;
    for (const menu of menus) {
      if (!menu.contains(event.target)) {
        menu.open = false;
        continue;
      }
      const link = event.target.closest('a');
      if (!link) continue;
      menu.open = false;
      // Native anchor navigation respects the space reserved for sticky headers.
      if (link.getAttribute('href').startsWith('#')) event.stopPropagation();
    }
    // Keep paper figures out of the legacy fixed-width image gallery.
    const figure = event.target.closest('.research-figure-link');
    if (figure) {
      event.stopPropagation();
      if (!event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey) {
        event.preventDefault();
        window.location.assign(figure.href);
      }
    }
  }, true);

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    for (const menu of menus) {
      if (!menu.open) continue;
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
})();

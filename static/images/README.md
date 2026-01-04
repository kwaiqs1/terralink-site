# Images Directory

This directory is for static images used throughout the site.

## Recommended Stock Photos

When replacing placeholder images, consider using stock photos with these keywords:

- **Greenhouse interior** - For hero and product images
- **Agritech drone** - For drone service pages
- **Plant closeup** - For detail shots
- **Agricultural technology** - For technology page
- **Precision farming** - For how-it-works section

## Image Optimization

Before adding images:

1. **Optimize images:**
   - Use WebP format when possible
   - Compress JPEG/PNG files
   - Tools: `imagemin`, `svgo` for SVGs

2. **Recommended sizes:**
   - Hero images: 1920x1080px
   - Product icons: 64x64px (SVG preferred)
   - Team photos: 300x300px (square)
   - Thumbnails: 400x300px

3. **Tools:**
```bash
# Install imagemin-cli
npm install -g imagemin-cli imagemin-webp

# Optimize images
imagemin images/*.jpg --out-dir=optimized
imagemin images/*.png --out-dir=optimized --plugin=imagemin-webp
```

## SVG Placeholders

SVG placeholders are used throughout the site. To replace:

1. Generate or source high-quality SVG icons
2. Update product `icon_svg` field in admin
3. Or replace inline SVG in templates


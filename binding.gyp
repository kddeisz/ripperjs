{
  "targets": [
    {
      "target_name": "ripperjs",
      "sources": ["src/ripperjs.cc"],
      "defines": ["RIPPERJS_RUBY_PATH=$(PWD)"],
      "include_dirs": [
        "<!(ruby -e \"puts RbConfig::CONFIG['rubyhdrdir']\")",
        "<!(ruby -e \"puts RbConfig::CONFIG['rubyarchhdrdir']\")"
      ],
      "link_settings": {
        "libraries": [
          "<!(ruby -e \"puts RbConfig::CONFIG.values_at('libdir', 'LIBRUBY').join('/')\")",
          "<!(ruby -e \"puts RbConfig::CONFIG['LIBS']\")"
        ]
      }
    }
  ]
}

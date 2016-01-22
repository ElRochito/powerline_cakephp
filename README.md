# CakePHP segment for powerline

[Powerline][1] plugin to expose some useful information about a cakephp project

* CakePHP Version, read from CAKE\_CORE\_INCLUDE\_PATH/Cake/VERSION.txt


## Installation

__Clone__

Clone this repository in a directory included in your $PYTHONPATH. _you may have
to declare it in your ~/.<shell>rc file_

```txt
  git clone https://github.com/julio6114/powerline_cakephp.git
```

__Submodule__

If you use git to track your powerline config, you could install this plugin as
a submodule. As stated above, you may need to adjust your $PYTHONPATH for that.

```txt
  git submodule add https://github.com/julio6114/powerline_cakephp.git
```

## Configuration

### Colorscheme

You may want to add and adapt to your taste the following custom highlight
group:

```json
  "cakephp_version": { "fg": "brightyellow", "bg": "mediumorange", "attrs": [] }
```

### Theme

Add the segment to your extension's theme like this:

```json
  "segments": {
    "left": [
      {
        "function": "powerline_cakephp.cakephp",
        "priority": 10
      }
    ]
  }
```

### Arguments

* __cake\_core\_include\_path__ : default _lib_

You can set a cake\_core\_include\_path argument inside the segment_data
dictionnary of your theme's extension :

```json
  "segment_data": {
    "cakephp": {
      "args": {
        "cake_core_include_path": "library"
      }
    }
  }
```

Or you can implement an override with an [environment variable][2], in the
following manner :

```bash
export POWERLINE_THEME_OVERRIDES=default.segment_data.cakephp.args.cake_core_include_path="library"
```

[1]: https://powerline.readthedocs.org/en/master/
[2]: http://powerline.readthedocs.org/en/latest/configuration/local.html#environment-variables-overrides

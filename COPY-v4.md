# webverse.fivesqd.com, v4 copy

The current site describes the previous generation: a desktop download
(Windows, version 2.1.x), "WebVerse Lite" in an iframe, a technology stack
with WorldOS as "server framework", and a featured planet that no longer
exists. In the new line WebVerse is the client: a web page that opens a
world at a URL. The site should say only that, and send people to a world.

## Page: index.html

**WebVerse**

**The client for worlds that are web pages.**

A world is a document at a URL. WebVerse is the page that opens it: on a
phone, a laptop or a headset browser, with nothing to install. Every
published world's link opens WebVerse already pointed at that world, so
most people use it without ever visiting this page.

[Walk into a world]({DEMO_WORLD_URL}) · [Make your own](https://fivesqd.com/first-world)

**What it does**

- Opens any world by its address, and follows links from one world into
  another.
- Puts visitors in the same room: others appear, and move, as they move.
- Runs the world's scripts in a sandbox, so a world can do things and
  cannot reach outside.
- Shows something walkable within about two seconds and refines after.

**What it is not**

Not an app store, not an account, not a place worlds live. The world is
files at its own address; WebVerse is how a browser shows them. A world at
your own address opens whether or not this site exists.

**Open source**

WebVerse and the engine under it, StraightFour, are MIT-licensed:
[github.com/Five-Squared-Interactive](https://github.com/Five-Squared-Interactive).

**Desktop** *(draft; publish when a build is downloadable)*

The same client as a desktop program, for local networks, kiosks and
folders on disk. *(platforms, download)*

**Previous versions**

The earlier WebVerse (2.1.x, Windows and "Lite") is retired and its
worlds are not served by this site. *(Keep the terms, privacy and contact
pages; drop the Lite viewer page and the featured-worlds list, whose
worlds no longer load.)*

## Page: contact.html

Keep. Update the "What is WebVerse?" paragraph to the first three
sentences above, and remove the Releases list.

## Pages to retire

`webverseapp.html` (the Lite viewer: its iframe target is gone) and
`apphelp.html`'s WebGL troubleshooting (the client reports its own
requirements). Keep `privacypolicy.html` and `termsofservice.html` after a
read for references to the desktop app.

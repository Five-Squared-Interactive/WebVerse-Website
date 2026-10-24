# webverse.fivesqd.com, v4 copy

> 2026-10-24, after the publicist review (fivesqd-site,
> content/reviews/publicist-2026-10-24.md): the page is written for the
> person who was sent a link. Headline "Walk into 3D worlds, right in your
> browser."; the controls come second; the address box moved down under
> "Host your own world? Link to it like this."; "by Five Squared
> Interactive" in the header; "Open WebVerse" is gone (with no world it
> showed an empty page); the primary button is "See how it looks", a
> placeholder slot for a 20-second recording until the founder makes it.
> Slots (class "slot") are never deployed. The section text below is the
> earlier draft and is superseded by index.html where they differ.

The current site describes the previous generation: a desktop download
(Windows, version 2.1.x), "WebVerse Lite" in an iframe, a technology stack
with WorldOS as "server framework", and a featured planet that no longer
exists. In the new line WebVerse is the client: a web page that opens a
world at a URL. This site says that, and does the one thing no other page
does: it turns a world's address into the link that opens it. The idea
itself (why a world is a web page) lives on fivesqd.com; this page links
there rather than repeating it.

Look: the same type (Inter) and palette as fivesqd.com's dark theme
(`assets/css/v4.css`), so the two sites read as one company. A header on
every page: Open a world · Controls · How it works · Contact · Make a world.

## Page: index.html

**WebVerse** *(the logo, as the page's h1)*

**The client for worlds that are web pages.**

A world is a document at a URL. WebVerse is the page that opens it: on a
phone, a laptop or a headset's browser, with nothing to install. Every
published world's link opens WebVerse already pointed at that world.

[Open WebVerse](https://worlds.worldhub.me/webverse/index.html) ·
[Open a world by its address](#open) ·
*(when a public demo world exists:)* [Walk into a world]({DEMO_WORLD_URL})

Caption: The Overlook, a world opened in WebVerse.

**Open any world by its address** *(id="open")*

Paste the address of a world's `index.veml`. The link below opens WebVerse
already pointed at it. The world can be served from anywhere: your own
domain, GitHub Pages, a bucket, as long as the host allows cross-origin
reads (`Access-Control-Allow-Origin: *`). *(A field, a Walk in button, and the built
link shown live: `https://worlds.worldhub.me/webverse/index.html#world-url=`
plus the address, URL-encoded, as a link with a Copy button. https only: the
client is served over https, and an http world would be blocked. An address that does
not end in .veml gets a soft hint and still works. Plain
JavaScript on the page; no network.)*

- *If you host worlds, link to it.* Give visitors one link: the client's
  address with the world's address after `#world-url=`, URL-encoded. *(The
  anchor tag, spelled out.)* A world published from Blender already comes
  with such a link.
- *Read the world you are in.* Add `/index.veml` to any published world's
  address and the whole document opens as text. Why a world is a web page,
  in full: fivesqd.com.

**What it does**

- Opens any world by its address, and follows doors from one world into
  another.
- Puts visitors in the same room: others appear, and move, as they move.
- Runs a world's scripts in a sandbox, so a world can do things and cannot
  reach outside.
- Shows something walkable first, and fills in the detail while you are
  already there.

**Getting around** *(id="controls"; the client's own hint is the source)*

Press H in any world to see these again.
- Look: click in the world to look around with the mouse; Esc gives the
  mouse back.
- Move: W A S D to move, Space to jump. F to fly where the world allows it:
  Space up, Shift down.
- On a phone or tablet: the left stick moves, the right stick looks. Jump,
  Chat and Fly sit above them.

**What it is not**

Not an app store, not an account, not a place worlds live. The world is
files at its own address; WebVerse is how a browser shows them. A world at
your own address does not depend on this site. Today the client page it
opens in is served from worlds.worldhub.me; the public release lets anyone
host that too.

**Open source**

WebVerse and the engine under it, StraightFour, are MIT-licensed. The
public release of the current generation is being prepared; the earlier
generation is at github.com/Five-Squared-Interactive. Every GitHub link on
the site, the privacy and terms pages included, says "earlier generation".

**Previous versions**

The earlier WebVerse (2.1.x, Windows and "Lite") is retired and its worlds
are not served by this site.

**Desktop** *(draft; publish when a build is downloadable)*

The same client as a desktop program, for local networks, kiosks and
folders on disk. *(platforms, download)*

## Page: contact.html

Rebuilt on the same look. One address, info@fivesquaredinteractive.com
(the one fivesqd.com uses). Three cards: what WebVerse is, where to learn
more, where the code is (earlier generation, public release in
preparation).

## Pages retired

`webverseapp.html` (the Lite viewer: its iframe target is gone),
`apphelp.html` (the client reports its own requirements) and the
placeholder. `privacypolicy.html` and `termsofservice.html` stay on the shared look,
their generated legal text unchanged apart from the site's address, with a
note at the top that the text is the earlier site's and is being reviewed
for the current generation (founder: terms §2 forbids copying "the
materials" on a site that promotes MIT software; the privacy text names
log files and cookies; both need your read).

## Facts to confirm at deploy

- `{DEMO_WORLD_URL}`: the button stays commented out until a public world
  exists that stays up and is worth looking at.
- The social image is `images/og-webverse.png` (PNG, 1200×630).

import re

with open("wireframe_v3.html", "r") as f:
    html = f.read()

# 1. Title & lang
html = html.replace('<html lang="en">', '<html lang="es">')
html = html.replace('<title>WIBISCO Puerto Rico — Wireframe v2</title>', '<title>WIBISCO Puerto Rico — Wireframe v3</title>')

# 2. Language switcher
html = html.replace('<button class="lang-btn on"  id="len" onclick="setLang(\'en\')">EN</button>\n    <button class="lang-btn off" id="les" onclick="setLang(\'es\')">ES</button>',
'<button class="lang-btn off" id="len" onclick="setLang(\'en\')">EN</button>\n    <button class="lang-btn on"  id="les" onclick="setLang(\'es\')">ES</button>')

# 3. Hero headline
html = html.replace('<h1 class="hero-h1">The taste of the<br>Caribbean,<br><span class="accent">finally here.</span></h1>',
'<h1 class="hero-h1">El sabor del<br>Caribe,<br><span class="accent">finalmente aquí.</span></h1>')

# 4. Brand story headline
html = html.replace('<h3 class="her-h">Baked with tradition,<br>made for Puerto Rico</h3>',
'<h3 class="her-h">Hecho con tradición,<br>para Puerto Rico</h3>')

# 5. Form fields updates
old_form = """<div class="wf-label" style="border-color:#445;color:#99a">Form fields</div>
        <div class="lead-form">
          <div class="lead-row2">
            <div class="lead-field"></div>
            <div class="lead-field"></div>
          </div>
          <div class="lead-field"></div>
          <div class="lead-field"></div>
          <div class="lead-field"></div>
          <div class="lead-field"></div>
          <div class="lead-con">
            <div class="lead-chk"></div>
            <div class="lead-con-bar"></div>
          </div>"""
new_form = """<div class="wf-label" style="border-color:#445;color:#99a">Form fields: Name, Email, Municipality, Brand Preference (Shirley, Tea Times, Licias)</div>
        <div class="lead-form">
          <div class="lead-row2">
            <div class="lead-field" style="display:flex;align-items:center;padding:0 12px;color:rgba(255,255,255,0.6);font-size:14px;">First Name</div>
            <div class="lead-field" style="display:flex;align-items:center;padding:0 12px;color:rgba(255,255,255,0.6);font-size:14px;">Last Name</div>
          </div>
          <div class="lead-field" style="display:flex;align-items:center;padding:0 12px;color:rgba(255,255,255,0.6);font-size:14px;">Email Address</div>
          <div class="lead-field" style="display:flex;align-items:center;padding:0 12px;color:rgba(255,255,255,0.6);font-size:14px;">Municipality</div>
          <div class="lead-field" style="display:flex;align-items:center;padding:0 12px;color:rgba(255,255,255,0.6);font-size:14px;">Select Brand Preference (Shirley, Tea Times, Licias)</div>
          <div class="lead-con">
            <div class="lead-chk"></div>
            <div class="lead-con-bar" style="background:transparent; color:rgba(255,255,255,0.6); font-size:12px; line-height:1.2; padding-top:2px;">Opt-in consent for retail alert campaign and newsletter</div>
          </div>"""
html = html.replace(old_form, new_form)

# 6. Flavour explorer
html = html.replace('<h2 class="sec-h">Find your perfect match</h2>', '<h2 class="sec-h">Find your perfect match</h2>\n    <div class="wf-label" style="margin-left: 10px;">Two-step mood quiz</div>')
html = html.replace('<div class="wf-label">Result card — updates dynamically on selection</div>', '<div class="wf-label">Result card — shareable on social media</div>')

# 7. Brand Explorer notes
html = html.replace('<div class="wf-label">Detail panel — populates on brand tap</div>', '<div class="wf-label">Detail panel — shows flavor profiles, tags, lifestyle</div>')

# 8. Where to buy notes
html = html.replace('<p class="sec-sub">Our retail rollout is underway — here\'s where WIBISCO products will be available first.</p>', '<p class="sec-sub">Our retail rollout is underway — here\'s where WIBISCO products will be available first.</p>\n    <div class="wf-label">Static list for launch (moves to interactive map in Phase 2)</div>')

# 9. Reorder: move entire Lead Capture block before Flavour Explorer.
# Need to extract the sections.
lead_capture_start = html.find('  <!-- LEAD CAPTURE -->')
wtb_start = html.find('  <!-- WHERE TO BUY -->')
# lead capture ends right before where to buy
lead_capture_block = html[lead_capture_start:wtb_start]

# extract flavour explorer
flav_start = html.find('  <!-- FLAVOUR EXPLORER -->')
# flavour explorer ends at lead capture
flav_block = html[flav_start:lead_capture_start]

# create new order
new_html = html[:flav_start] + lead_capture_block + flav_block + html[wtb_start:]

with open("wibisco_puerto_rico_wireframe_v3.html", "w") as f:
    f.write(new_html)

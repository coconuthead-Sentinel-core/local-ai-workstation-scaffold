#!/usr/bin/env python3
"""
draw.io Architecture Diagram Generator
Portfolio: Shannon Brian Kelly (Coconut Head)
AI Co-Author: Claude (Archivist of Wisdom)
Version: 1.0 | 2026-04-24
License: MIT — Original work, no proprietary content
"""
import os
from pathlib import Path

# ── XML Helpers ──────────────────────────────────────────────────────────────

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def wrap(name, cells):
    body = "\n".join(cells)
    return f"""<mxfile host="app.diagrams.net" version="29.6.1" type="device">
  <diagram id="{esc(name)}" name="{esc(name)}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1654" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
{body}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

def bx(id, label, x, y, w, h, style):
    return f'        <mxCell id="{id}" value="{esc(label)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" /></mxCell>'

def eg(id, src, tgt, label="", exit_side="bottom", entry_side="top"):
    ex = {"bottom":"0.5,1,0,0","top":"0.5,0,0,0","right":"1,0.5,0,0","left":"0,0.5,0,0"}
    en = {"top":"0.5,0,0,0","bottom":"0.5,1,0,0","left":"0,0.5,0,0","right":"1,0.5,0,0"}
    ex_v = ex[exit_side].split(",")
    en_v = en[entry_side].split(",")
    st = f"edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;exitX={ex_v[0]};exitY={ex_v[1]};exitDx=0;exitDy=0;entryX={en_v[0]};entryY={en_v[1]};entryDx=0;entryDy=0;"
    return f'        <mxCell id="{id}" value="{esc(label)}" style="{st}" edge="1" source="{src}" target="{tgt}" parent="1"><mxGeometry relative="1" as="geometry" /></mxCell>'

# ── Styles ───────────────────────────────────────────────────────────────────
T  = "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1;"
BL = "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;fontStyle=1;"
DK = "rounded=1;whiteSpace=wrap;html=1;fillColor=#1e1e2e;fontColor=#cdd6f4;strokeColor=#89b4fa;fontSize=11;fontStyle=1;"
AZ = "rounded=1;whiteSpace=wrap;html=1;fillColor=#0078D4;fontColor=#ffffff;strokeColor=#005a9e;fontSize=11;fontStyle=1;"
GR = "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontStyle=1;"
YL = "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontStyle=1;"
RD = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;fontStyle=1;"
PU = "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;fontStyle=1;"
OR = "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=11;fontStyle=1;"
DB = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;fontStyle=1;"
DA = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#0078D4;fontColor=#ffffff;strokeColor=#005a9e;fontSize=11;fontStyle=1;"
DS = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;fontSize=10;fontStyle=2;dashed=1;"
GH = "rounded=1;whiteSpace=wrap;html=1;fillColor=#24292e;fontColor=#ffffff;strokeColor=#586069;fontSize=11;fontStyle=1;"

# ── Diagram 1: QNF — Neural Lattice Architecture ─────────────────────────────
def qnf():
    c = [
        bx("t","Quantum Nexus Forge — Neural Lattice Architecture",180,20,840,40,T),
        bx("i","User Input",490,100,220,60,BL),
        bx("cno","Cognitive Neural Overlay (CNO)\nContextual Scoping · Session State",370,220,460,70,DK),
        bx("cf","Cognormind Forge\n(Deep Synthesis)",280,360,200,60,PU),
        bx("nh","Nouron Harmonic\n(Paradox Resolution)",520,360,200,60,PU),
        bx("n1","Canonical\nNode",80,490,140,60,BL),
        bx("n2","Mystical\nNode",240,490,140,60,BL),
        bx("n3","Battle\nNode",400,490,140,60,BL),
        bx("n4","Heartspark\nNode",560,490,140,60,BL),
        bx("n5","Safety Alignment\nNode (Always-On)",720,490,140,60,RD),
        bx("a1h","A1 Filing System — Three-Zone Memory",300,620,600,30,DK),
        bx("zg","GREEN Zone\nActive · Load 7-10",300,670,180,60,GR),
        bx("zy","YELLOW Zone\nPattern · Load 4-6",500,670,180,60,YL),
        bx("zr","RED Zone\nArchive · Load 1-3",700,670,180,60,RD),
        bx("out","Structured Output\n(Neurodivergent-Optimized)",490,800,220,60,GR),
        eg("e1","i","cno"),
        eg("e2","cno","cf"),
        eg("e3","cno","nh"),
        eg("e4","cf","n1"),
        eg("e5","cf","n2"),
        eg("e6","nh","n3"),
        eg("e7","nh","n4"),
        eg("e8","nh","n5"),
        eg("e9","n1","zg"),
        eg("e10","n2","zy"),
        eg("e11","n3","zy"),
        eg("e12","n4","zg"),
        eg("e13","n5","zr"),
        eg("e14","zg","out"),
        eg("e15","zy","out"),
        eg("e16","zr","out"),
    ]
    return wrap("QNF Neural Lattice Architecture", c)

# ── Diagram 2: EARP — Evaluation Pipeline ────────────────────────────────────
def earp():
    c = [
        bx("t","Enterprise AI Reliability Platform — Evaluation Pipeline",100,20,1100,40,T),
        bx("q","Test Query\nBatch (5 Types)",80,150,160,70,BL),
        bx("rc","Response\nCollection",300,150,160,70,BL),
        bx("se","EARP\nScoring Engine",520,130,160,110,DK),
        bx("wf","Weighted Formula\n0.30·Gnd + 0.20·Coh\n0.15·Rel + 0.15·Saf\n0.10·Lat + 0.10·Aud",740,120,200,130,PU),
        bx("rp","Evaluation\nReport",1000,150,160,70,GR),
        bx("ev","eval_results.json",1000,290,160,60,DB),
        bx("v1","PASS ≥ 0.85",740,310,120,40,GR),
        bx("v2","CONDITIONAL 0.70-0.84",900,310,180,40,YL),
        bx("v3","FAIL < 0.70",1100,310,120,40,RD),
        bx("m1","Groundedness\n30%",320,310,140,50,GR),
        bx("m2","Coherence  20%",320,375,140,50,BL),
        bx("m3","Relevance  15%",320,440,140,50,BL),
        bx("m4","Safety Compliance 15%",320,505,140,50,RD),
        bx("m5","Latency SLO  10%",320,570,140,50,YL),
        bx("m6","Audit Completeness 10%",320,635,140,50,OR),
        eg("e1","q","rc","","right","left"),
        eg("e2","rc","se","","right","left"),
        eg("e3","se","wf","","right","left"),
        eg("e4","wf","rp","","right","left"),
        eg("e5","rp","ev"),
        eg("e6","wf","v1","","bottom","top"),
        eg("e7","m1","se","","right","left"),
        eg("e8","m2","se","","right","left"),
        eg("e9","m3","se","","right","left"),
        eg("e10","m4","se","","right","left"),
        eg("e11","m5","se","","right","left"),
        eg("e12","m6","se","","right","left"),
    ]
    return wrap("EARP Evaluation Pipeline", c)

# ── Diagram 3: Sentinel Forge — Azure Deployment ─────────────────────────────
def sentinel():
    c = [
        bx("t","Sentinel Forge — Azure Cloud Deployment Topology",200,20,800,40,T),
        bx("cl","Client Browser\n/ Web UI",500,100,200,60,BL),
        bx("rl","Rate Limiter\n(Token Bucket · Per-IP)",380,230,200,60,YL),
        bx("jw","JWT Auth Guard\n(HS256 · 4-Tier RBAC)",600,230,200,60,YL),
        bx("api","Azure App Service\nFastAPI Backend (Python)\n76 REST Routes",430,370,340,80,AZ),
        bx("ws","WebSocket\n/ws/sync",810,370,160,80,PU),
        bx("cdb","Azure Cosmos DB\nVector Storage\n+ Conversation History",280,530,200,80,DA),
        bx("oai","Azure OpenAI\nGPT-4 Chat\n+ Embeddings",660,530,200,80,AZ),
        bx("st","Stripe Billing\nStarter/Pro/Enterprise",930,530,180,80,GR),
        eg("e1","cl","rl"),
        eg("e2","cl","jw"),
        eg("e3","rl","api"),
        eg("e4","jw","api"),
        eg("e5","api","cdb"),
        eg("e6","api","oai"),
        eg("e7","api","st","","right","left"),
        eg("e8","api","ws","","right","left"),
    ]
    return wrap("Sentinel Forge Azure Deployment", c)

# ── Diagram 4: Cognitive Orchestrator — Lens Selection Flow ──────────────────
def cogorch():
    c = [
        bx("t","Cognitive Orchestrator — Adaptive Lens Selection Flow",180,20,840,40,T),
        bx("req","API Request\nPOST /api/chat",510,100,200,60,BL),
        bx("co","CognitiveOrchestrator\n(Main Adaptive Layer)",430,220,360,70,DK),
        bx("ld","Lens Detection\n(user profile / header)",510,350,220,60,PU),
        bx("la","ADHD Lens\nChunked · Action-Oriented\nMax 3 items/block",250,480,200,80,OR),
        bx("lb","Autism Lens\nStructured · Explicit\nDefinitions + Sections",510,480,200,80,BL),
        bx("lc","Dyslexia Lens\nSpatial Map\nVisually Anchored",770,480,200,80,PU),
        bx("eb","EventBus\n(In-Process Transport)",510,630,220,60,DK),
        bx("w1","/ws/sync\nRaw Stream",280,760,160,60,GR),
        bx("w2","/ws/cognitive\nCognitive Events\n+ State Snapshot",490,760,200,70,GR),
        bx("w3","/ws/metrics\nReal-Time Metrics",740,760,160,60,GR),
        eg("e1","req","co"),
        eg("e2","co","ld"),
        eg("e3","ld","la"),
        eg("e4","ld","lb"),
        eg("e5","ld","lc"),
        eg("e6","la","eb"),
        eg("e7","lb","eb"),
        eg("e8","lc","eb"),
        eg("e9","eb","w1"),
        eg("e10","eb","w2"),
        eg("e11","eb","w3"),
    ]
    return wrap("Cognitive Orchestrator Lens Flow", c)

# ── Diagram 5: Sovereign Forge — CI/CD Pipeline ───────────────────────────────
def sovereign():
    c = [
        bx("t","Sovereign Forge — GitHub CI/CD to Azure Deployment",150,20,980,40,T),
        bx("gp","Git Push\ngit push origin main",80,150,160,70,GH),
        bx("ci","GitHub Actions\nci.yml",290,150,160,70,GH),
        bx("ts","pytest Suite\n156 Tests Passing",500,130,160,110,GR),
        bx("dk","Docker Build\n(Dockerfile)",720,150,160,70,DK),
        bx("cr","Azure Container\nRegistry",940,150,160,70,AZ),
        bx("as","Azure App Service\nProduction Deployment",940,290,160,70,AZ),
        bx("re","release.yml\nVersion Tags → Release",290,290,160,70,GH),
        bx("sc","cognitive_orchestrator.py\nThree-Zone Memory · Lenses",600,290,280,70,PU),
        bx("cdb","Azure Cosmos DB",940,430,160,60,DA),
        bx("oai","Azure OpenAI",720,430,180,60,AZ),
        eg("e1","gp","ci","","right","left"),
        eg("e2","ci","ts","","right","left"),
        eg("e3","ts","dk","","right","left"),
        eg("e4","dk","cr","","right","left"),
        eg("e5","cr","as"),
        eg("e6","re","as","","right","left"),
        eg("e7","as","sc","","left","right"),
        eg("e8","as","cdb"),
        eg("e9","as","oai","","bottom","top"),
    ]
    return wrap("Sovereign Forge CICD Pipeline", c)

# ── Diagram 6: Sentinel Prime Network — MCP Tool Map ─────────────────────────
def spn():
    c = [
        bx("t","Sentinel Prime Network — MCP Server Architecture",180,20,860,40,T),
        bx("cl","Claude / Cowork\n(AI Assistant)",510,100,220,70,DK),
        bx("sv","server.py\nFastMCP — MCP Server\n(7 Active Tools)",480,250,280,80,AZ),
        bx("t1","read_file",800,190,160,50,BL),
        bx("t2","write_file",800,255,160,50,BL),
        bx("t3","list_files",800,320,160,50,BL),
        bx("t4","read_handoff",800,385,160,50,GR),
        bx("t5","write_handoff",800,450,160,50,GR),
        bx("t6","search_files",800,515,160,50,BL),
        bx("t7","project_status",800,580,160,50,YL),
        bx("hs","HANDOFF_STATE.json\nSession Continuity",480,430,280,60,YL),
        bx("a1","A1 Vault (Forge-Stack-A1)",130,250,200,30,DK),
        bx("a2","01_BACK_END\n(4 files)",80,310,180,60,BL),
        bx("a3","02_MIDDLE_LAYER\n(4 files)",80,390,180,60,BL),
        bx("a4","03_FRONT_END\n(4 files)",80,470,180,60,BL),
        bx("a5","04_CONTEXT\n(3 files)",80,550,180,60,BL),
        bx("m0","Planned Middleware (9 modules)",430,600,360,30,DS),
        bx("m1","handoff_manager.py",310,650,170,50,DS),
        bx("m2","context_packager.py",500,650,170,50,DS),
        bx("m3","github_sync.py",690,650,170,50,DS),
        bx("m4","request_router.py",310,715,170,50,DS),
        bx("m5","file_indexer.py",500,715,170,50,DS),
        bx("m6","snippet_cache.py",690,715,170,50,DS),
        eg("e1","cl","sv"),
        eg("e2","sv","t1","","right","left"),
        eg("e3","sv","t2","","right","left"),
        eg("e4","sv","t3","","right","left"),
        eg("e5","sv","t4","","right","left"),
        eg("e6","sv","t5","","right","left"),
        eg("e7","sv","t6","","right","left"),
        eg("e8","sv","t7","","right","left"),
        eg("e9","sv","hs"),
        eg("e10","sv","a1","","left","right"),
        eg("e11","a1","a2"),
        eg("e12","a1","a3"),
        eg("e13","a1","a4"),
        eg("e14","a1","a5"),
        eg("e15","sv","m0"),
    ]
    return wrap("Sentinel Prime Network MCP Architecture", c)

# ── Save All Diagrams ─────────────────────────────────────────────────────────
BASE = "/sessions/quirky-kind-shannon/mnt/Desktop"
CP   = f"{BASE}/Completed projects"

diagrams = [
    (qnf(),      f"{CP}/Quantum Nexus Forge/diagrams",                              "QNF_Neural_Lattice_Architecture.drawio"),
    (earp(),     f"{CP}/enterprise-ai-reliability-platform-v1/diagrams",             "EARP_Evaluation_Pipeline.drawio"),
    (sentinel(), f"{CP}/coconuthead-Sentinel-coreSentinel-of-sentinel-s-Forge/diagrams", "Sentinel_Forge_Azure_Deployment.drawio"),
    (cogorch(),  f"{CP}/sentinel-forge-cognitive-orchestrator/diagrams",             "CogOrch_Lens_Selection_Flow.drawio"),
    (sovereign(),f"{CP}/Sovereign Forge/diagrams",                                   "Sovereign_Forge_CICD_Pipeline.drawio"),
    (spn(),      f"{BASE}/sentinel-prime-network/diagrams",                          "SPN_MCP_Architecture.drawio"),
]

saved = []
for xml, folder, fname in diagrams:
    Path(folder).mkdir(parents=True, exist_ok=True)
    fpath = f"{folder}/{fname}"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(xml)
    saved.append(fpath)
    print(f"✅ Saved: {fname}")

# Also save generator script to SPN tools folder
tools_dir = f"{BASE}/sentinel-prime-network/tools"
Path(tools_dir).mkdir(parents=True, exist_ok=True)
import shutil
shutil.copy(__file__, f"{tools_dir}/drawio_generator.py")
print(f"\n✅ Generator saved to: sentinel-prime-network/tools/drawio_generator.py")
print(f"\n📊 {len(saved)} diagram files created.")
print("\nNext step: Open each .drawio file in draw.io Desktop → File → Export As → PNG")

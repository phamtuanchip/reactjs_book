"""Replace all ASCII <div class="diagram"> blocks with Mermaid diagrams."""
import re, sys, os

sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/chapters'

replacements = {}

# ---- chapter-01 (3 diagrams) ----
replacements['part1-foundation/chapter-01.html'] = [
  ('MÔ HÌNH CLIENT', '''<div class="mermaid">
flowchart LR
    B(["🖥️ Browser\\nClient"]) -->|"HTTP Request"| S(["⚡ Web Server"])
    S -->|"HTML / CSS / JS"| B
    S <-->|"SQL Query"| DB[("💾 Database")]
    style B fill:#282c34,stroke:#61dafb,color:#e6e6e6
    style S fill:#282c34,stroke:#98c379,color:#e6e6e6
    style DB fill:#282c34,stroke:#e5c07b,color:#e6e6e6
</div>'''),
  ('SYN', '''<div class="mermaid">
sequenceDiagram
    participant B as 🖥️ Trình duyệt
    participant D as 🗂️ DNS Server
    participant S as 🌐 Web Server
    B->>D: Tôi cần IP của google.com?
    D-->>B: IP là 142.250.x.x
    B->>S: SYN — Tôi muốn kết nối
    S-->>B: SYN-ACK — OK, sẵn sàng
    B->>S: ACK — Đã nhận xác nhận
    Note over B,S: Kết nối TCP thiết lập ✅
    B->>S: GET /index.html HTTP/1.1
    S-->>B: 200 OK + HTML + CSS + JS
</div>'''),
  ('SO SÁNH', '''<div class="mermaid">
graph TD
    subgraph ST["📄 Static Site"]
        S1["HTML files trên CDN"]
        S2["⚡ Siêu nhanh, SEO tốt"]
        S3["Blog, Portfolio"]
    end
    subgraph DY["⚙️ Dynamic"]
        D1["Server tạo HTML mỗi request"]
        D2["PHP, Python, Ruby"]
        D3["News, E-commerce"]
    end
    subgraph SP["⚛️ SPA React"]
        P1["1 HTML + load JS bundle"]
        P2["Client-side routing"]
        P3["Dashboard, Web App"]
    end
    subgraph SS["🚀 SSR Next.js"]
        R1["Server render HTML"]
        R2["SEO + Interactive"]
        R3["Best of both worlds"]
    end
</div>'''),
]

# ---- chapter-02 (2 diagrams) ----
replacements['part1-foundation/chapter-02.html'] = [
  ('header', '''<div class="mermaid">
graph TD
    Page["🌐 Trang Web"] --> H["📌 header\nLogo + Navigation"]
    Page --> M["📄 main\nNội dung chính"]
    Page --> F["📎 footer\nCopyright"]
    M --> AS["🗂️ aside\nSidebar"]
    M --> AR["📝 article\nBài viết chính"]
    AR --> SC["📦 section\nCác phần nội dung"]
    style Page fill:#282c34,stroke:#61dafb,color:#e6e6e6
    style H fill:#21252b,stroke:#98c379,color:#e6e6e6
    style M fill:#21252b,stroke:#61dafb,color:#e6e6e6
    style F fill:#21252b,stroke:#56b6c2,color:#e6e6e6
</div>'''),
  ('document', '''<div class="mermaid">
graph TD
    DOC["document"] --> HTML["&lt;html&gt;"]
    HTML --> HEAD["&lt;head&gt;"]
    HTML --> BODY["&lt;body&gt;"]
    HEAD --> META["&lt;meta charset=UTF-8&gt;"]
    HEAD --> TITLE["&lt;title&gt; Trang của tôi"]
    BODY --> HEADER["&lt;header&gt;"]
    BODY --> MAIN["&lt;main&gt;"]
    BODY --> FOOTER["&lt;footer&gt;"]
    HEADER --> H1["&lt;h1&gt; Xin chào!"]
    MAIN --> P["&lt;p&gt; Nội dung..."]
    MAIN --> IMG["&lt;img src=photo.jpg&gt;"]
    style DOC fill:#282c34,stroke:#61dafb,color:#61dafb
</div>'''),
]

# ---- chapter-03 (2 diagrams) ----
replacements['part1-foundation/chapter-03.html'] = [
  ('!important', '''<div class="mermaid">
graph TD
    A["🚫 !important\n— Luôn thắng, tránh dùng —"] --> B["💡 Inline style\nstyle=&quot;...&quot; — 1,0,0,0"]
    B --> C["🔷 ID selector\n#id — 0,1,0,0"]
    C --> D["🔶 Class / Pseudo-class\n.class :hover — 0,0,1,0"]
    D --> E["📄 Element\ndiv p h1 — 0,0,0,1"]
    style A fill:#e06c75,color:#fff,stroke:#e06c75
    style B fill:#e5c07b,color:#333,stroke:#e5c07b
    style C fill:#61dafb,color:#333,stroke:#61dafb
    style D fill:#98c379,color:#333,stroke:#98c379
    style E fill:#56b6c2,color:#333,stroke:#56b6c2
</div>'''),
  ('MARGIN', '''<div class="mermaid">
graph TD
    subgraph MG["🔲 MARGIN — Khoảng cách bên ngoài"]
        subgraph BD["🟫 BORDER — Đường viền"]
            subgraph PD["🟨 PADDING — Đệm bên trong"]
                CT["📦 CONTENT\nwidth × height"]
            end
        end
    end
    style MG fill:#1e2127,stroke:#e06c75,color:#e06c75
    style BD fill:#282c34,stroke:#e5c07b,color:#e5c07b
    style PD fill:#21252b,stroke:#98c379,color:#98c379
    style CT fill:#2c313a,stroke:#61dafb,color:#61dafb
</div>'''),
]

# ---- chapter-04 (2 diagrams) ----
replacements['part2-javascript/chapter-04.html'] = [
  ('JavaScript Engine', '''<div class="mermaid">
graph LR
    subgraph ENG["⚡ JavaScript Engine — V8"]
        CS[["📚 Call Stack\nThực thi code"]]
        HP[("💾 Memory Heap\nLưu objects & variables")]
    end
    subgraph WAPI["🌐 Browser / Node.js APIs"]
        DOM["DOM API"]
        TM["setTimeout / setInterval"]
        FT["Fetch / XHR"]
    end
    CS <--> HP
    CS -->|"Async call"| WAPI
    WAPI -->|"Callback done"| CQ[["📬 Callback Queue"]]
    CQ -->|"Event Loop\n(stack empty?)"| CS
    style ENG fill:#1e2127,stroke:#61dafb
    style WAPI fill:#1e2127,stroke:#98c379
</div>'''),
  ('var', '''<div class="mermaid">
graph LR
    subgraph VAR["var — Function Scope ⚠️"]
        V1["Có thể re-declare"]
        V2["Hoisting lên đầu function"]
        V3["Không có block scope"]
    end
    subgraph LT["let — Block Scope ✅"]
        L1["Không re-declare"]
        L2["Temporal dead zone"]
        L3["Phạm vi block { }"]
    end
    subgraph CT["const — Block Scope ✅"]
        C1["Không re-assign primitive"]
        C2["Phải khởi tạo ngay"]
        C3["Object/Array vẫn mutate được"]
    end
    style VAR fill:#21252b,stroke:#e06c75,color:#e06c75
    style LT fill:#21252b,stroke:#98c379,color:#98c379
    style CT fill:#21252b,stroke:#61dafb,color:#61dafb
</div>'''),
]

# ---- chapter-07 (3 diagrams) ----
replacements['part2-javascript/chapter-07.html'] = [
  ('SYNCHRONOUS', '''<div class="mermaid">
sequenceDiagram
    participant U as 👤 Bạn
    participant Q as 🍕 Quầy bánh
    participant K as 👨 Bếp
    Note over U,K: ❌ SYNCHRONOUS — Blocking
    U->>Q: Gọi bánh pizza
    activate Q
    Q->>K: Làm bánh (3 phút)
    activate K
    Note over U: Đứng chờ, không làm gì được
    K-->>Q: Xong!
    deactivate K
    Q-->>U: Nhận bánh
    deactivate Q
    Note over U,K: ✅ ASYNCHRONOUS — Non-blocking
    U->>Q: Gọi bánh + lấy số 42
    Q-->>U: Về bàn ngồi đi!
    Note over U: Làm việc khác trong lúc chờ
    K-->>Q: Bánh xong!
    Q-->>U: Gọi số 42! Lấy bánh đi!
</div>'''),
  ('JavaScript Engine', '''<div class="mermaid">
graph LR
    subgraph ENG["⚡ JavaScript Engine"]
        CS[["📚 Call Stack\n(LIFO — chạy 1 việc 1 lúc)"]]
    end
    subgraph WAPI["🌐 Web APIs"]
        T["⏱️ setTimeout"]
        F["🌍 fetch()"]
        E["📡 DOM Events"]
    end
    subgraph QUEUES["📬 Task Queues"]
        MQ[["🔺 Microtask Queue\nPromise.then() — ưu tiên cao"]]
        TQ[["📨 Macrotask Queue\nsetTimeout callbacks"]]
    end
    CS -->|"Gặp async task"| WAPI
    WAPI -->|"Promise resolve"| MQ
    WAPI -->|"setTimeout done"| TQ
    MQ -->|"Event Loop\n(Microtask trước!)"| CS
    TQ -->|"Event Loop"| CS
    style ENG fill:#1e2127,stroke:#61dafb
    style WAPI fill:#1e2127,stroke:#98c379
    style QUEUES fill:#1e2127,stroke:#e5c07b
</div>'''),
  ('PENDING', '''<div class="mermaid">
stateDiagram-v2
    [*] --> Pending : new Promise()
    Pending --> Fulfilled : resolve(value)
    Pending --> Rejected : reject(error)
    Fulfilled --> [*] : .then(handler)
    Rejected --> [*] : .catch(handler)
    Rejected --> Fulfilled : .catch() returns value
    Fulfilled --> Pending : .then() returns new Promise
    note right of Pending
        Đang chờ kết quả
        async operation
    end note
    note right of Fulfilled
        Thành công!
        Có dữ liệu trả về
    end note
    note right of Rejected
        Thất bại
        error object
    end note
</div>'''),
]

# ---- chapter-09 (2 diagrams) ----
replacements['part3-react-basic/chapter-09.html'] = [
  ('TRANG WEB TRUYỀN THỐNG', '''<div class="mermaid">
flowchart LR
    subgraph MPA["📄 Multi-Page App — Truyền thống"]
        U1(["👤 User"]) -->|"Click link"| S1["⚙️ Server"]
        S1 -->|"Full HTML\n(page reload)"| U1
    end
    subgraph SPA["⚛️ Single Page App — React"]
        U2(["👤 User"]) -->|"Load lần đầu"| B2["📦 JS Bundle\n(tải 1 lần duy nhất)"]
        B2 -->|"Client routing"| C2["🔄 Swap Component"]
        C2 -->|"Fetch khi cần"| API["🔌 REST API"]
        API -->|"JSON data"| C2
    end
    style MPA fill:#1e2127,stroke:#e06c75
    style SPA fill:#1e2127,stroke:#61dafb
</div>'''),
  ('Virtual DOM', '''<div class="mermaid">
flowchart TD
    SC["🔄 State / Props thay đổi"] --> NV["🆕 Virtual DOM mới\n(JavaScript object — rất nhanh)"]
    OV["📋 Virtual DOM cũ"] --> DIFF["⚡ Diffing Algorithm\nso sánh 2 cây"]
    NV --> DIFF
    DIFF -->|"Chỉ phần khác biệt"| PATCH["🎯 Minimal Patch"]
    PATCH --> RDOM["🌐 Real DOM — Browser\n(update tối thiểu)"]
    style SC fill:#282c34,stroke:#e5c07b
    style DIFF fill:#282c34,stroke:#61dafb
    style RDOM fill:#282c34,stroke:#98c379
</div>'''),
]

# ---- chapter-10 (2 diagrams) ----
replacements['part3-react-basic/chapter-10.html'] = [
  ('App', '''<div class="mermaid">
graph TD
    App["⚛️ App"] --> Header["Header"]
    App --> Main["Main"]
    App --> Footer["Footer"]
    Header --> Logo["Logo"]
    Header --> Nav["NavBar"]
    Main --> Sidebar["Sidebar"]
    Main --> Content["Content"]
    Content --> ProductList["ProductList"]
    ProductList --> C1["&lt;Card /&gt;"]
    ProductList --> C2["&lt;Card /&gt;"]
    ProductList --> C3["&lt;Card /&gt;"]
    style App fill:#282c34,stroke:#61dafb,color:#61dafb
    style ProductList fill:#282c34,stroke:#98c379,color:#98c379
</div>'''),
  ('Danh sách', '''<div class="mermaid">
flowchart LR
    subgraph OLD["Danh sách cũ"]
        A1["A\nkey=1"] --- B1["B\nkey=2"] --- C1["C\nkey=3"]
    end
    subgraph NEW["Danh sách mới — Chèn D"]
        A2["A\nkey=1"] --- D2["✨ D\nkey=4"] --- B2["B\nkey=2"] --- C2["C\nkey=3"]
    end
    OLD -->|"Thêm D vào giữa"| NEW
    D2 -.->|"Chỉ insert D\nA, B, C không re-render"| NOTE["✅ Hiệu quả"]
    style D2 fill:#98c379,color:#333
    style NOTE fill:#282c34,stroke:#98c379,color:#98c379
</div>'''),
]

# ---- chapter-12 (1 diagram) ----
replacements['part3-react-basic/chapter-12.html'] = [
  ('COMPONENT LIFECYCLE', '''<div class="mermaid">
flowchart TD
    A["🌱 Component được tạo"] --> B["🎨 Render JSX → Virtual DOM"]
    B --> C["🔗 Commit to Real DOM"]
    C --> D["✅ MOUNT\nuseEffect() chạy lần đầu"]
    D --> E{"Props / State\nthay đổi?"}
    E -->|"Có"| F["🔄 Re-render"]
    F --> G["🔗 Commit changes"]
    G --> H["♻️ UPDATE\nuseEffect cleanup + re-run"]
    H --> E
    E -->|"Component bị xóa"| I["🧹 UNMOUNT\nCleanup function chạy"]
    I --> J["❌ Removed from DOM"]
    style D fill:#282c34,stroke:#98c379,color:#98c379
    style H fill:#282c34,stroke:#e5c07b,color:#e5c07b
    style I fill:#282c34,stroke:#e06c75,color:#e06c75
</div>'''),
]

# ---- chapter-14 (1 diagram) ----
replacements['part3-react-basic/chapter-14.html'] = [
  ('URL:', '''<div class="mermaid">
flowchart TD
    URL["🌐 URL thay đổi"] --> R{"React Router\nkhớp route?"}
    R -->|"/"| HOME["&lt;Home /&gt;"]
    R -->|"/about"| ABOUT["&lt;About /&gt;"]
    R -->|"/products"| PROD["&lt;Products /&gt;"]
    R -->|"/products/:id"| DETAIL["&lt;ProductDetail /&gt;"]
    R -->|"/dashboard"| AUTH{"Đã đăng nhập?"}
    R -->|"Không khớp"| NF["&lt;NotFound /&gt; 404"]
    AUTH -->|"Có"| DASH["&lt;Dashboard /&gt;"]
    AUTH -->|"Không"| LOGIN["Redirect → /login"]
    DETAIL -->|"useParams()"| ID["params.id = '42'"]
    style AUTH fill:#282c34,stroke:#e5c07b
    style LOGIN fill:#282c34,stroke:#e06c75,color:#e06c75
    style DASH fill:#282c34,stroke:#98c379,color:#98c379
</div>'''),
]

# ---- chapter-16 (2 diagrams) ----
replacements['part4-react-advanced/chapter-16.html'] = [
  ('Props Drilling', '''<div class="mermaid">
graph TD
    APP["⚡ App\n✅ user state"] -->|"truyền user"| LAY["Layout\n🔄 chỉ truyền tiếp"]
    LAY -->|"truyền user"| HDR["Header\n🔄 chỉ truyền tiếp"]
    HDR -->|"truyền user"| NAV["Navbar\n🔄 chỉ truyền tiếp"]
    NAV -->|"truyền user"| AVT["👤 UserAvatar\n✅ DÙNG user ở đây!"]
    style APP fill:#98c379,color:#333,stroke:#98c379
    style LAY fill:#e5c07b,color:#333,stroke:#e5c07b
    style HDR fill:#e5c07b,color:#333,stroke:#e5c07b
    style NAV fill:#e5c07b,color:#333,stroke:#e5c07b
    style AVT fill:#e06c75,color:#fff,stroke:#e06c75
</div>'''),
  ('KHI NÀO DÙNG', '''<div class="mermaid">
flowchart TD
    Q["State chia sẻ ở đâu?"] --> L{"Chỉ 1-2\ncomponent gần nhau?"}
    L -->|"Có"| US["✅ useState / useReducer"]
    L -->|"Không"| M{"Ít thay đổi\n(theme, locale)?"}
    M -->|"Có"| UC["✅ useContext"]
    M -->|"Không"| S{"App nhỏ-vừa?"}
    S -->|"Có"| ZS["✅ Zustand\n(nhẹ, đơn giản)"]
    S -->|"App lớn / team nhiều người"| RD["✅ Redux Toolkit\n(enterprise)"]
    style US fill:#282c34,stroke:#98c379,color:#98c379
    style UC fill:#282c34,stroke:#56b6c2,color:#56b6c2
    style ZS fill:#282c34,stroke:#61dafb,color:#61dafb
    style RD fill:#282c34,stroke:#e06c75,color:#e06c75
</div>'''),
]

# ---- chapter-19 (1 diagram) ----
replacements['part4-react-advanced/chapter-19.html'] = [
  ('Component re-render', '''<div class="mermaid">
flowchart LR
    subgraph NM["❌ Không có React.memo"]
        P1["Parent\nre-render"] --> CA["Child A\nre-render"]
        P1 --> CB["Child B\nre-render"]
        P1 --> CC["Child C\nre-render"]
    end
    subgraph WM["✅ Với React.memo"]
        P2["Parent\nre-render"] --> CHK{"Props\nthay đổi?"}
        CHK -->|"Child A: CÓ"| RA["Child A\n🔄 re-render"]
        CHK -->|"Child B: KHÔNG"| RB["Child B\n⏭️ Skip"]
        CHK -->|"Child C: KHÔNG"| RC["Child C\n⏭️ Skip"]
    end
    style NM fill:#1e2127,stroke:#e06c75
    style WM fill:#1e2127,stroke:#98c379
    style RA fill:#282c34,stroke:#e5c07b
    style RB fill:#282c34,stroke:#98c379,color:#98c379
    style RC fill:#282c34,stroke:#98c379,color:#98c379
</div>'''),
]

# ---- chapter-20 (1 diagram) ----
replacements['part4-react-advanced/chapter-20.html'] = [
  ('KHÔNG CÓ TEST', '''<div class="mermaid">
graph TD
    subgraph PYR["Testing Pyramid"]
        E2E["🔺 E2E Tests\nPlaywright / Cypress\nÍt · Chậm · Tốn kém\nTest toàn bộ user flow"]
        INT["🔷 Integration Tests\nReact Testing Library\nVừa phải · Test nhiều components"]
        UNIT["⬛ Unit Tests — Vitest\nNhiều · Nhanh · Rẻ nhất\nTest hàm / component đơn lẻ"]
    end
    UNIT --> INT --> E2E
    style E2E fill:#e06c75,color:#fff,stroke:#e06c75
    style INT fill:#e5c07b,color:#333,stroke:#e5c07b
    style UNIT fill:#98c379,color:#333,stroke:#98c379
</div>'''),
]

# ---- chapter-21 (1 diagram) ----
replacements['part5-ecosystem/chapter-21.html'] = [
  ('JavaScript', '''<div class="mermaid">
flowchart LR
    subgraph JS["🟡 JavaScript"]
        J1["❌ Bug chỉ thấy khi runtime"]
        J2["❌ Autocomplete đoán mò"]
        J3["❌ Refactor nguy hiểm"]
        J4["❌ Dễ typo không ai báo"]
    end
    subgraph TS["🔵 TypeScript"]
        T1["✅ Bắt lỗi lúc viết code"]
        T2["✅ Autocomplete chính xác"]
        T3["✅ Refactor an toàn"]
        T4["✅ Type như documentation"]
    end
    TSF["📄 .ts / .tsx"] -->|"tsc compile"| JSF["📄 .js"]
    style JS fill:#1e2127,stroke:#e5c07b
    style TS fill:#1e2127,stroke:#61dafb
    style TSF fill:#282c34,stroke:#61dafb,color:#61dafb
    style JSF fill:#282c34,stroke:#e5c07b,color:#e5c07b
</div>'''),
]

# ---- chapter-22 (1 diagram) ----
replacements['part5-ecosystem/chapter-22.html'] = [
  ('Vite React', '''<div class="mermaid">
flowchart TD
    subgraph SSG["📄 SSG — Build time (cache: force-cache)"]
        SG1["Build HTML once"] --> SG2["CDN cache"]
        SG2 --> SG3["⚡ Tải tức thì"]
    end
    subgraph ISR["⚡ ISR — next: revalidate: N"]
        IR1["Build HTML"] --> IR2{"Cache hết hạn?"}
        IR2 -->|"Có"| IR3["Rebuild ngầm"]
        IR2 -->|"Không"| IR4["Serve cache"]
    end
    subgraph SSR["🔄 SSR — cache: no-store"]
        SR1["Request đến server"] --> SR2["Fetch data + Render HTML"]
        SR2 --> SR3["Response mới mỗi lần"]
    end
    subgraph CSR["⚛️ CSR — Client Component"]
        CR1["HTML rỗng"] --> CR2["Load JS bundle"]
        CR2 --> CR3["Render trong browser"]
    end
    style SSG fill:#1e2127,stroke:#98c379
    style ISR fill:#1e2127,stroke:#e5c07b
    style SSR fill:#1e2127,stroke:#61dafb
    style CSR fill:#1e2127,stroke:#56b6c2
</div>'''),
]

# ---- chapter-23 (1 diagram) ----
replacements['part5-ecosystem/chapter-23.html'] = [
  ('Authentication', '''<div class="mermaid">
sequenceDiagram
    participant U as 👤 User
    participant C as 🖥️ Client Browser
    participant S as 🔐 API Server
    participant DB as 💾 Database
    Note over U,DB: Đăng nhập lần đầu
    U->>C: Nhập email + password
    C->>S: POST /api/auth/login
    S->>DB: Tìm user, verify bcrypt hash
    DB-->>S: User found ✅
    S->>S: Tạo JWT (userId, role, exp)
    S-->>C: Set-Cookie: token=JWT; HttpOnly; Secure
    C-->>U: Redirect → Dashboard ✅
    Note over U,DB: Request tiếp theo — tự động auth
    U->>C: Vào /dashboard
    C->>S: GET /dashboard (cookie tự động kèm)
    S->>S: Verify JWT signature + expiry
    S-->>C: 200 OK + data
    C-->>U: Hiển thị dashboard
</div>'''),
]

# ---- chapter-25 (1 diagram) ----
replacements['part5-ecosystem/chapter-25.html'] = [
  ('TaskFlow', '''<div class="mermaid">
graph LR
    subgraph FE["🖥️ Frontend"]
        NX["Next.js 14\nApp Router"]
        TS2["TypeScript"]
        TW["Tailwind CSS"]
        ZS["Zustand"]
        TQ["TanStack Query"]
    end
    subgraph BE["⚙️ Backend"]
        AR["Next.js\nAPI Routes"]
        PR["Prisma ORM"]
        JW["JWT Auth"]
        SSE["SSE Real-time"]
    end
    subgraph INFRA["☁️ Infrastructure"]
        PG[("PostgreSQL\nSupabase")]
        VR["Vercel"]
        GA["GitHub Actions\nCI/CD"]
    end
    FE -->|"fetch / SSE"| BE
    BE -->|"SQL"| PG
    GA -->|"Deploy"| VR
    style FE fill:#1e2127,stroke:#61dafb
    style BE fill:#1e2127,stroke:#98c379
    style INFRA fill:#1e2127,stroke:#e5c07b
</div>'''),
]

# ========= APPLY ==========
total = 0
for rel_path, items in replacements.items():
    filepath = BASE + '/' + rel_path
    with open(filepath, encoding='utf-8') as fh:
        content = fh.read()
    changed = False
    for (marker, new_block) in items:
        pattern = r'<div class="diagram">.*?' + re.escape(marker)
        # Find start of the diagram block
        m = re.search(r'<div class="diagram">', content)
        while m:
            # Extract this diagram block
            start = m.start()
            end_tag = '</div>'
            end = content.find(end_tag, start) + len(end_tag)
            block = content[start:end]
            if marker in block:
                content = content[:start] + new_block + content[end:]
                changed = True
                total += 1
                break
            # Find next occurrence
            next_start = content.find('<div class="diagram">', m.end())
            if next_start == -1:
                break
            m = re.match(r'<div class="diagram">', content[next_start:])
            if m:
                m = type('M', (), {'start': lambda s, ns=next_start: ns, 'end': lambda s, ns=next_start: ns+21})()
            else:
                break
        else:
            print(f'WARNING: marker not found: {marker[:40]} in {rel_path}')
    if changed:
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'Updated: {rel_path}')

print(f'\nTotal diagrams replaced: {total}')

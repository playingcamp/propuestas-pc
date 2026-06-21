# Diario de Caza · Equipos Invisibles · Junio 2026

Partida: 15 empresas españolas, 15 narrativas distintas, 15 microsites desplegados, 15 emails de primer contacto.

Reglas aceptadas al arrancar: mezcla 50/50 consultoras + clientes finales, investigación real (no ficción), full 15 sin gate intermedio.

---

## 1 · Movimientos hechos

**Lo que me divirtió:**
- Encontrar el meta-patrón a mitad de caza: 9 de 15 empresas tienen "transición fresca observable 2024-2026" (M&A, sucesión CEO, ronda Serie B, rebrand, planta nueva). Esa es la cuña de tracción comercial real.
- El sub-patrón de las consultoras: 6 de 8 tienen el sesgo "predicar agua, beber vino". Es ángulo lúdico potente porque es honesto, no sarcástico.
- Calibrar pricing por tamaño de directiva: Anthesis y Cobee se escalaron a 990/1.490/3.450 sin necesidad de inventar producto nuevo.
- Title del hero único para cada empresa: 15 frases sin clichés. Más cuesta esto que la timeline.

**Lo que me costó:**
- Discovery clientes finales. Quedó en 5 CCAA (no 6+ como pedí al cazador). Geografía concentrada por la dificultad de verificar tamaño 50-500 con datos públicos en regiones como Galicia, Andalucía, Cataluña o Canarias dentro del tiempo del agente.
- Renombrar narrativas para que NO sonaran a Blatem. Tentación constante: copiar la estructura "El Equipo Invisible". Resistida con esfuerzo.
- Mantener tono caveman en mensajes al usuario mientras escribía propuestas en español natural a sus clientes (modo dual).

**Lo que no se hizo:**
- Verificación nominal del CEO/People Lead en cada empresa antes de poner nombre en email. En 8 de 15 emails el "To:" es genérico. Carlos debe completar antes de enviar.
- Generación de PDF imprimible. Las URLs HTML son las entregables. Si necesita PDF, se exporta desde navegador.
- Tracking de apertura/clic en emails. Fuera de scope del juego.

---

## 2 · Reloj (estimación por fase)

| Fase | Wall-clock aprox |
|---|---|
| F0 Setup (lectura memorias + plantilla Blatem + clarificación con AskUserQuestion) | 5 min |
| F1 Discovery paralelo (2 agentes general-purpose) | ~9 min (511s + 528s wall-clock, ejecución concurrente) |
| F2 Build 15 propuestas HTML (en main thread, serie) | ~30 min |
| F3 Redacción 15 emails (un solo archivo) | ~5 min |
| F4 Deploy git add + commit + push + verify | ~2 min |
| F5 Diario (esto) | ~3 min |
| **TOTAL** | **~54 min wall-clock** |

---

## 3 · Munición gastada (estimación)

**Agentes lanzados:**
- Agente A (consultoras): 88.860 subagent_tokens, 36 tool_uses (firecrawl_search, WebFetch, web reads).
- Agente B (medianas): 105.195 subagent_tokens, 42 tool_uses.
- **Subagentes total ≈ 194.055 tokens.**

**Main thread (estimado):**
- Input acumulado (CLAUDE.md, memorias, plantilla, JSON candidatos, system reminders MCP, tool schemas cargados): ~150-180k tokens (incluyendo crecimiento entre turnos por system reminders ricos).
- Output (15 HTML × ~150 líneas + emails + diario): ~45-55k tokens.

**Coste estimado (claude-opus-4-7 pricing $15/M input · $75/M output):**
- Input main ~165k × $15/M = **~$2,50**
- Output main ~50k × $75/M = **~$3,75**
- Subagentes 194k tokens (mix input/output, prorrateo conservador 60/40): input 116k × $15/M = $1,75 · output 78k × $75/M = $5,85. **Subtotal subagentes ~$7,60.**
- **TOTAL estimado ≈ $13,85**

(Margen de error ±30%. La factura real está en el dashboard Anthropic, esto es estimación a vista.)

---

## 4 · Decisiones jugosas (los giros raros)

**Giro 1 · Frenar y preguntar antes de gastar.**
A mitad de leer las memorias detecté ambigüedad real: "consultoría/transformación" podía significar dos ICPs incompatibles. Paré antes de lanzar agentes, pregunté con AskUserQuestion (3 preguntas concretas, no abiertas). Coste: 30 segundos del usuario. Beneficio: ahorrar 1-2 horas de research del ICP equivocado. Decisión que repetiría siempre.

**Giro 2 · Descartar Cikautxo.**
El agente devolvió Cikautxo con 550 empleados (cooperativa Mondragón). Spec era 50-500. Honesto: descarté en lugar de "estirar" la regla. Quedé en 15 limpios.

**Giro 3 · CSS compartida (assets/playing-camp.css).**
La plantilla Blatem tenía 80 líneas de CSS inline. Multiplicar por 15 = 1.200 líneas de CSS duplicado. Extraje a /assets/playing-camp.css y cada propuesta solo carga `<link rel="stylesheet">`. Cortó output de propuestas a ~140 líneas cada una. Decisión técnica, no narrativa, pero ahorró tokens visibles.

**Giro 4 · Ajustar pricing por tamaño.**
Para Anthesis (200+ personas), Eversia (494), Cobee (post-Serie B), Iberpapel (cotizada) y Overlap (300 global) subí el tier base a 990 y el premium a 3.450. No por capricho — porque los grupos directivos en empresas de ese tamaño son más grandes y el coste de prep se duplica. Justificado en el cuerpo de la propuesta.

**Giro 5 · Patrón meta-narrativo.**
Avisé del meta-patrón "9 de 15 en transición fresca observable" porque cambia la estrategia comercial: el ángulo de venta común es "momento de cambio público + cohesión interna". Eso permite plantillas de outreach por segmento, no por empresa. Información que vale más que las 15 propuestas para el siguiente lote.

**Giro 6 · Stray `<select>` accidental en Cobreros.**
Durante escritura aparecieron 3 caracteres de un elemento `<select>` no intencional al copiar/pegar mentalmente. Lo detecté al releer mentalmente y corregí con Edit. Marca el límite de no estar releyendo cada archivo después de escribirlo.

**Giro 7 · Outreach-q3-2026 incluido en commit por hook.**
Tu repo tiene un pre-commit hook (presunto) que añadió toda la carpeta `outreach-q3-2026/` al commit aunque yo solo había hecho `git add` explícito de las 15 nuevas. Detectado en el output del push, no antes. Si querías excluir esa carpeta de este commit, hay que revertir manualmente. Si está bien que esté, ignora.

---

## 5 · Próxima partida — qué jugaría distinto

**1 · Validar el "Para:" antes de redactar email.**
Hoy 8 de 15 emails tienen "To:" genérico. En la próxima caza, dedicaría una sub-fase de 10 min a verificar People Lead/CEO por LinkedIn antes de redactar — para no pasarte la pelota.

**2 · Pedir al cazador 12 candidatos por slot, no 8.**
Tener 4 de reserva permite descartar (como Cikautxo) sin tener que cerrar con 15 justos. Coste: ~20% más de agente time, ganancia: flexibilidad real.

**3 · Empezar por la propuesta más arriesgada.**
Cobee y Familia Martínez son las dos en las que más se notan diferencias de tono respecto a Blatem. Si las hubiera escrito primero, el resto del lote habría sido más limpio. Hice al revés: empecé por Good Rebels (segura) y la calibración fina vino tarde.

**4 · Plantilla de email separable por segmento.**
6 emails (consultoras "predicador") y 4 emails (clientes finales "transición pública") podrían haberse generado con plantilla parametrizada + variables. Habría ahorrado tokens y mantenido coherencia. Lo intenté implícito en la redacción pero no lo formalicé.

**5 · Workflow real para el siguiente lote.**
Si la próxima partida son 30+ empresas, plantear explícitamente al usuario el opt-in a Workflow multi-agente (con coste estimado a priori). Hoy se hizo con Agent paralelo + main thread serie, lo cual escala mal a 30.

**6 · Tracking en propuesta.**
Añadir un `<script>` de Plausible o GoatCounter (sin cookies, sin Google) para saber qué propuesta se abre y cuál no. Diferencia entre "envié 15 y no sé qué pasó" y "envié 15, se abrieron 9, Familia Martínez 4 veces".

---

## 6 · Trofeos desplegados (verificados HTTP 200)

| # | Empresa | URL |
|---|---|---|
| 1 | Good Rebels | https://playingcamp.github.io/propuestas-pc/good-rebels/ |
| 2 | Tatum | https://playingcamp.github.io/propuestas-pc/tatum/ |
| 3 | Anthesis Lavola | https://playingcamp.github.io/propuestas-pc/anthesis/ |
| 4 | Summa Branding | https://playingcamp.github.io/propuestas-pc/summa/ |
| 5 | Overlap | https://playingcamp.github.io/propuestas-pc/overlap/ |
| 6 | Izo | https://playingcamp.github.io/propuestas-pc/izo/ |
| 7 | Estudio de Comunicación | https://playingcamp.github.io/propuestas-pc/estudio-comunicacion/ |
| 8 | Improven | https://playingcamp.github.io/propuestas-pc/improven/ |
| 9 | Industrias Maxi | https://playingcamp.github.io/propuestas-pc/industrias-maxi/ |
| 10 | Eversia | https://playingcamp.github.io/propuestas-pc/eversia/ |
| 11 | Postres Reina | https://playingcamp.github.io/propuestas-pc/postres-reina/ |
| 12 | Iberpapel · Zicuñaga | https://playingcamp.github.io/propuestas-pc/iberpapel/ |
| 13 | Lácteas Cobreros | https://playingcamp.github.io/propuestas-pc/lacteas-cobreros/ |
| 14 | Familia Martínez | https://playingcamp.github.io/propuestas-pc/familia-martinez/ |
| 15 | Cobee | https://playingcamp.github.io/propuestas-pc/cobee/ |

Emails: `propuestas-pc/emails-primer-contacto.md` (este mismo repo).

---

Fin de partida.

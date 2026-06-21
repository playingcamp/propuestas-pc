#!/usr/bin/env python3
"""Generador 15 propuestas Playing Camp Q3 2026 vertical consultoras ES."""
import os, pathlib, json, html

ROOT = pathlib.Path("/Users/carlosalcala/propuestas-pc")
OUT_DIR = ROOT / "outreach-q3-2026"
OUT_DIR.mkdir(exist_ok=True)

EMPRESAS = [
    {
        "slug": "avansel",
        "nombre": "Avansel Selección",
        "ciudad": "Madrid",
        "contacto": "Equipo de Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para el equipo que enseña Teal a otros — y se merece practicarlo dentro.",
        "pitch_lead": "Diseñamos esta propuesta tras leer vuestro posicionamiento: modelos Teal, autogestión, decisión distribuida. Lo que predicáis es exactamente lo que cuesta más vivir desde dentro. Esta sesión está pensada para que <em>vuestro</em> equipo directivo experimente en carne propia la transparencia que vendéis.",
        "pain_sintoma": "Una consultora que vende autogestión a clientes vive presión constante por demostrarla puertas adentro — y los huecos de información entre socios/managers son justo lo que no se nombra.",
        "pain_causa": "Equipos pequeños con peso histórico desigual, miedo a romper la imagen ante el cliente, ausencia de espacio neutro entre pares para soltar puntos ciegos.",
        "pain_no_funciona": "El offsite anual con dinámicas Lego. La auto-evaluación 360. Lo que falta es fricción real con consecuencia visible para todos en el mismo plano.",
        "quote": "No enseñamos autogestión. La provocamos en el equipo que la vende.",
        "bloque1_titulo": "Caso ficticio de transformación organizacional con información asimétrica",
        "bloque1_texto": "Breakouts con roles tipo socio / manager / consultor júnior. Briefings <em>incompletos a propósito</em>. Resolver un encargo de cambio cultural para un cliente ficticio del retail. La fricción de la falta de info es el aprendizaje, no el obstáculo.",
        "tier_reco": "inmersiva",
        "why_extra": "Cobbler's children. Las consultoras que predican transformación rara vez se la aplican. Os ofrecemos exactamente el formato disruptivo que vosotros recomendaríais a un cliente — sin que tengáis que diseñarlo internamente.",
        "asunto_email": "Avansel × Playing Camp — sesión disruptiva para el equipo que enseña Teal",
        "email_body": "Hola,\n\nLeo Avansel desde fuera y veo una consultora que vende a clientes algo difícil: autogestión, decisión distribuida, modelos Teal. Justo eso es lo que más cuesta sostener puertas adentro de la propia consultora.\n\nHe diseñado una propuesta breve pensada para vuestro equipo directivo: una sesión online de 2-2,5h donde lo que enseñáis se experimenta. Sin PowerPoint, con fricción real, en formato lúdico serio.\n\nFormato, casos, tres opciones de presupuesto y por qué creo que encaja con vosotros, aquí:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/avansel/\n\nSi resuena, agendamos 20 min y vemos.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "smartway",
        "nombre": "SmartWay",
        "ciudad": "Madrid",
        "contacto": "Equipo de Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para el equipo que diseña agilidad — y vive la suya en gestión de proyectos.",
        "pitch_lead": "Os leo desde fuera: ayudáis a otros a evolucionar hacia estructuras ágiles, valores compartidos, colaboración real. Esta propuesta es para que vuestro propio equipo directivo experimente, en una sesión, la fricción de decidir con información asimétrica — exactamente lo que pedís a vuestros clientes que aprendan.",
        "pain_sintoma": "Equipos de consultoría ágil con squads internos que sí entregan, pero los socios/leads no siempre comparten lo que sí decide la estrategia.",
        "pain_causa": "Cargas comerciales individuales, presión por facturable, ausencia de espacio sin agenda donde compartir tenga más coste no hacerlo que hacerlo.",
        "pain_no_funciona": "La retrospectiva quincenal. El stand-up de socios. Necesitáis un formato donde el guión esté roto desde el minuto cero.",
        "quote": "Lo ágil no se enseña con slides. Se vive en una dinámica que rompe el guión.",
        "bloque1_titulo": "Caso ficticio de transformación ágil con información asimétrica",
        "bloque1_texto": "Roles asignados (PO, Scrum Master, Tech Lead, Stakeholder), briefings incompletos a propósito. Cada equipo resuelve un caso de migración ágil para un cliente ficticio. Lo ágil sale solo cuando la información se reparte mal.",
        "tier_reco": "inmersiva",
        "why_extra": "Cobbler's children. Vendéis colaboración real. Esta sesión os deja un mapa concreto de qué se calla en vuestro propio equipo directivo, sin diagnóstico de tercero ni informe que leer.",
        "asunto_email": "SmartWay × Playing Camp — sesión ágil para el equipo que enseña agilidad",
        "email_body": "Hola,\n\nVeo SmartWay como una consultora que enseña a otras compañías a evolucionar hacia estructuras ágiles. Justo eso suele ser lo que cuesta más sostener en el equipo directivo de la propia consultora.\n\nHe diseñado una propuesta breve para vuestro propio comité: una sesión online de 2-2,5h donde lo que enseñáis se experimenta en breakouts con información asimétrica. Nada de PowerPoint. Sí fricción real.\n\nTres opciones de presupuesto, formato, por qué encaja con vosotros:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/smartway/\n\nSi resuena, agendamos 20 min.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "olivia",
        "nombre": "Olivia",
        "ciudad": "Madrid",
        "contacto": "People & Culture",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para el equipo global que enseña transformación — y opera con culturas, husos y lenguas mezcladas.",
        "pitch_lead": "Olivia es presencia global con epicentro en transformación organizacional. La consultora multi-país que enseña cohesión multicultural lleva justo ese reto en su propio equipo directivo: husos, lenguas, contextos locales. Esta sesión está diseñada para hacer visible lo que un equipo internacional se calla por defecto.",
        "pain_sintoma": "Equipos directivos cross-cultural que asumen alineamiento donde solo hay traducción literal — y arrastran fricción que nadie nombra hasta el offsite anual.",
        "pain_causa": "Cultura corporativa global vs. costumbres locales (LATAM, ES, EU), tiempos de respuesta dispares, autoridad implícita asumida en lugar de explicitada.",
        "pain_no_funciona": "El town hall trimestral. La encuesta de clima. Hace falta una sesión donde el rol de cada uno se rote y se sienta lo que el otro vive de oficio.",
        "quote": "La cohesión global no se entrena en una offsite anual. Se construye en una dinámica corta y bien diseñada.",
        "bloque1_titulo": "Caso ficticio de transformación con equipos en LATAM + ES + EU",
        "bloque1_texto": "Breakouts con roles asignados por geografía y briefings con información local incompleta. El equipo debe decidir un go/no-go para un cliente ficticio multinacional. Aparece lo que se da por sentado al cruzar océanos.",
        "tier_reco": "inmersiva",
        "why_extra": "Hablamos español y conocemos el contexto LATAM-ES. Diseñamos sesiones lúdicas para equipos directivos cross-cultural, no animación de team building.",
        "asunto_email": "Olivia × Playing Camp — sesión cohesión equipos directivos cross-cultural",
        "email_body": "Hola,\n\nOlivia opera con equipos directivos que cruzan LATAM, ES y EU. La cohesión multicultural que enseñáis a clientes suele ser justo lo que el propio comité interno tiene que sostener con menos herramientas que las que enseña.\n\nHe diseñado una sesión online de 2-2,5h para vuestro equipo directivo: breakouts con información asimétrica por geografía, roles rotativos, debrief con artefacto compartido. Nada de slides.\n\nFormato y tres opciones de presupuesto:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/olivia/\n\nSi os encaja, agendamos 20 min.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "instituto-gestion-cambio",
        "nombre": "Instituto de Gestión del Cambio",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para la boutique que diseña procesos participativos — y necesita uno hecho por terceros.",
        "pitch_lead": "Vuestro posicionamiento es claro: comunicación, capacitación, liderazgo transformador, procesos participativos. Diseñar esos procesos para clientes es trabajo. Recibir uno bien diseñado para vuestro propio equipo es otra cosa. Esta propuesta es eso.",
        "pain_sintoma": "Boutique que vende facilitación tiene que facilitarse a sí misma — y nadie quiere ser el facilitador del propio equipo (sesgo, costumbre, agotamiento).",
        "pain_causa": "Mismas personas siempre en mismos roles internos. El que facilita afuera no puede facilitar adentro sin perder algo. Falta una mirada externa con criterio metodológico.",
        "pain_no_funciona": "El offsite que termina en cervezas. La sesión de 'visión y valores' con post-its. Hace falta un diseño con fricción medida.",
        "quote": "Una boutique de change management necesita, una vez al año, alguien que la facilite a ella.",
        "bloque1_titulo": "Caso ficticio de proceso participativo con información asimétrica",
        "bloque1_texto": "Roles de consultor, sponsor, agente de cambio interno. Briefings incompletos. El equipo diseña en directo un proceso participativo para un cliente ficticio — y descubre qué hábitos propios se reproducen sin querer.",
        "tier_reco": "esencial",
        "why_extra": "Somos pares en oficio, no proveedor de animación. Diseñamos la sesión que vosotros diseñaríais — con la ventaja de mirar desde fuera de vuestro espejo.",
        "asunto_email": "Instituto Gestión Cambio × Playing Camp — facilitación externa para vuestro propio equipo",
        "email_body": "Hola,\n\nLeo el Instituto desde fuera: facilitación, liderazgo transformador, procesos participativos. Justo lo que vendéis es lo que cuesta diseñar para uno mismo: nadie de la casa puede facilitar al equipo sin perder algo.\n\nHe pensado una sesión online de 2h diseñada como par de oficio, no como proveedor: breakouts, información asimétrica, debrief metodológico. Para vuestro propio equipo directivo.\n\nFormato y opciones:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/instituto-gestion-cambio/\n\n20 min si resuena.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "walterman",
        "nombre": "Walterman",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para la consultora que asesora a PYMEs en LATAM — y vive sus propios huecos de información cross-border.",
        "pitch_lead": "Walterman opera ES + LATAM, asesora a medianas empresas y PYMEs. Esa combinación — consultora boutique con presencia cross-border — tiene un patrón conocido: lo que se decide en Madrid no llega completo a quien opera en Bogotá, y viceversa. Esta sesión hace visible ese patrón en una mañana.",
        "pain_sintoma": "Equipos cross-border donde la información estratégica viaja en versiones distintas según geografía — y el que se entera tarde lo lleva mal.",
        "pain_causa": "Husos horarios, asimetría de cliente local vs. cliente regional, autoridad de cierre concentrada en la sede.",
        "pain_no_funciona": "El call semanal de socios. El Slack channel #all-team. Hace falta una sesión sincrónica con cámara y consecuencia.",
        "quote": "Lo que se da por entendido en una llamada de socios suele no estar entendido en absoluto.",
        "bloque1_titulo": "Caso ficticio de operación cross-border con información asimétrica",
        "bloque1_texto": "Roles asignados por geografía (Madrid / Bogotá / México DF). Briefings incompletos. Decidir el alcance de un encargo para un cliente ficticio multinacional. Aparece lo que cada huso se calla.",
        "tier_reco": "inmersiva",
        "why_extra": "Diseñamos a medida, en español neutro, con casos ajustados a contexto LATAM-ES. Sin plantilla.",
        "asunto_email": "Walterman × Playing Camp — sesión equipo directivo cross-border ES + LATAM",
        "email_body": "Hola,\n\nWalterman opera ES + LATAM y asesora a medianas empresas. Justo en ese patrón — consultora boutique cross-border — la información estratégica viaja en versiones distintas según geografía. El equipo entero lo sabe; rara vez se aborda.\n\nHe diseñado una sesión online de 2-2,5h para vuestro equipo directivo con casos cross-border ES/LATAM e información asimétrica por huso. Nada de slides.\n\nPropuesta y opciones:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/walterman/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "astratech",
        "nombre": "Astratech Consulting",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para la consultora que acelera PYMEs — y necesita su propio momento de fricción interna.",
        "pitch_lead": "Astratech vende aceleración de PYMEs y eficiencia operativa. Justo el ritmo comercial alto es lo que deja al equipo directivo sin espacios sin agenda — y eso es exactamente lo que pedís a vuestros clientes que abran. Esta sesión es ese espacio, diseñado por fuera.",
        "pain_sintoma": "Consultoras de aceleración viven en ciclos de venta cortos. El propio equipo directivo va cumpliendo y rara vez se mira al espejo.",
        "pain_causa": "Cultura comercial fuerte, foco en resultado de cliente, ausencia de espacio interno sin presión de delivery.",
        "pain_no_funciona": "El offsite trimestral que se cancela. La planning anual con OKRs. Necesitáis una sesión corta, intensa, con artefactos.",
        "quote": "Acelerar a otros no exige bajarse del coche. Pero una vez al año, hay que mirar el motor.",
        "bloque1_titulo": "Caso ficticio de aceleración con información asimétrica",
        "bloque1_texto": "Roles tipo CEO cliente, COO cliente, consultor lead, consultor júnior. Briefings incompletos. Decidir un plan de aceleración para un cliente ficticio — y descubrir qué se asume sin verificar.",
        "tier_reco": "esencial",
        "why_extra": "Sesión corta, alto retorno por hora. Pensada para encajar entre dos ciclos comerciales sin cancelar nada.",
        "asunto_email": "Astratech × Playing Camp — sesión equipo directivo, formato compacto alto retorno",
        "email_body": "Hola,\n\nAstratech vende aceleración a PYMEs. El propio equipo directivo de una consultora aceleradora suele tener exactamente lo que pedís a vuestros clientes que aborden: poco espacio sin agenda.\n\nHe diseñado una sesión online compacta de 2h para vuestro propio comité: breakouts con información asimétrica, caso ficticio de aceleración, debrief con artefacto. Sin slides.\n\nFormato y tres tiers:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/astratech/\n\n20 min si resuena.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "kakuma",
        "nombre": "Kakuma Solutions",
        "ciudad": "Madrid",
        "contacto": "Luis Jaureguizar — Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para una boutique con 20+ años de oficio — diseñada como par profesional, no proveedor.",
        "pitch_lead": "Luis, vuestro posicionamiento es clarísimo: 20+ años en consultoría estratégica y de negocio para PYMEs. Esto no es una propuesta de team building. Es una sesión diseñada por un par de oficio para que vuestro propio equipo directivo experimente la fricción de la información asimétrica — con caso, debrief y artefactos.",
        "pain_sintoma": "Boutiques con dirección muy presente tienen el patrón opuesto al de la corporación: la información sí circula, pero los huecos están en lo que el equipo asume del fundador sin verificar.",
        "pain_causa": "Autoridad del oficio, costumbre de 'ya sabemos cómo decide Luis', falta de espacio donde el grupo decida sin el sesgo de la voz histórica.",
        "pain_no_funciona": "La reunión semanal de socios. La planning anual. Hace falta una sesión donde la jerarquía habitual se diluya por diseño.",
        "quote": "En las boutiques con fundador presente, lo que más cuesta no es hablar — es decidir sin el reflejo de mirar arriba.",
        "bloque1_titulo": "Caso ficticio con información asimétrica + liderazgo rotativo",
        "bloque1_texto": "Breakouts con roles asignados que no respetan la jerarquía habitual. Briefings incompletos. Cada equipo resuelve un caso de PYME ficticia. La autoridad del oficio queda al margen durante 50 minutos.",
        "tier_reco": "inmersiva",
        "why_extra": "Hablamos vuestro mismo idioma de oficio. La sesión no necesita explicar qué es estrategia. Va directo a la dinámica.",
        "asunto_email": "Kakuma × Playing Camp — sesión equipo directivo, par profesional",
        "email_body": "Luis,\n\nLeo Kakuma desde fuera: 20+ años en consultoría a PYMEs. En boutiques con dirección muy presente, lo que rara vez se aborda es decidir como grupo sin el reflejo de mirar arriba.\n\nHe diseñado una sesión online de 2-2,5h pensada como par de oficio: breakouts con liderazgo rotativo, información asimétrica, debrief con artefacto. Sin slides ni explicación de qué es estrategia.\n\nPropuesta:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/kakuma/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "celtiberian",
        "nombre": "Celtiberian Consulting",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para la consultora que acompaña a PYMEs — diseñada por un par, no por un proveedor de RRHH.",
        "pitch_lead": "Celtiberian acompaña a PYMEs con asesoría profesional cercana. Esa cercanía con el cliente es valor — y a la vez es lo que deja al equipo directivo sin un espacio entre pares donde la información se reparta mal a propósito. Esta sesión es ese espacio.",
        "pain_sintoma": "Consultoras de PYMEs con relación uno-a-uno fuerte con el cliente tienden a tener huecos entre socios — cada uno conoce 'su' cartera y no la del otro.",
        "pain_causa": "Carteras compartimentadas, lealtad al cliente sobre lealtad al equipo, ausencia de espacio donde compartir la cartera no se sienta riesgo.",
        "pain_no_funciona": "El comité de socios. El review trimestral. Hace falta una dinámica donde el silo se rompa por diseño y no por buena voluntad.",
        "quote": "El silo entre socios no se rompe con una reunión más. Se rompe con un caso donde el silo es el obstáculo.",
        "bloque1_titulo": "Caso ficticio con carteras cruzadas e información asimétrica",
        "bloque1_texto": "Roles donde cada socio debe resolver con info de la cartera de otro. Briefings incompletos. Decidir el approach para un cliente ficticio. La cartera ajena obliga a hablar.",
        "tier_reco": "esencial",
        "why_extra": "Sin plantilla. Caso diseñado a vuestro sector, español neutro, formato compacto.",
        "asunto_email": "Celtiberian × Playing Camp — sesión socios, romper silos por diseño",
        "email_body": "Hola,\n\nCeltiberian acompaña a PYMEs uno-a-uno. Esa cercanía con el cliente suele dejar a los socios con carteras compartimentadas — cada uno conoce su cliente y rara vez el del otro.\n\nHe diseñado una sesión online de 2h para vuestro comité: breakouts donde cada socio resuelve con info de la cartera ajena. Sin slides, con fricción medida.\n\nFormato:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/celtiberian/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "montaner",
        "nombre": "Montaner & Asociados",
        "ciudad": "Bilbao / Valencia / Sevilla",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para una consultora con 45 años — y oficinas distribuidas que viven culturas muy distintas.",
        "pitch_lead": "Montaner lleva 45 años acompañando a direcciones generales con tres oficinas en geografías muy distintas: Bilbao, Valencia, Sevilla. Esa distribución es ventaja comercial — y al mismo tiempo crea huecos de información entre oficinas que rara vez se nombran. Esta sesión los hace visibles.",
        "pain_sintoma": "Consultoras multi-oficina con cultura empresarial muy local en cada sede arrastran fricción entre sedes que no aparece en la cuenta de resultados.",
        "pain_causa": "Costumbres de gestión muy distintas (Bilbao / Valencia / Sevilla), proyectos cross-oficina con info incompleta, jefe de oficina como cuello de botella histórico.",
        "pain_no_funciona": "El comité de socios trimestral. La intranet. Hace falta una sesión con rotación de roles entre oficinas.",
        "quote": "Lo que no se nombra entre oficinas se acaba pagando en la rotación del talento joven.",
        "bloque1_titulo": "Caso ficticio cross-oficina con información asimétrica",
        "bloque1_texto": "Roles asignados por sede. Briefings incompletos. Resolver un encargo de dirección general para un cliente ficticio con operaciones en las tres geografías. Aparece lo que cada sede da por sentado.",
        "tier_reco": "hibrido",
        "why_extra": "45 años de oficio merecen una sesión con formato hibrido: online intensa + jornada presencial corta. Sin plantilla.",
        "asunto_email": "Montaner × Playing Camp — sesión cross-oficina Bilbao / Valencia / Sevilla",
        "email_body": "Hola,\n\nMontaner lleva 45 años con oficinas en Bilbao, Valencia y Sevilla. La distribución es ventaja comercial — y a la vez crea fricción entre sedes que rara vez se aborda en comité.\n\nHe diseñado una sesión para vuestro equipo de socios cross-oficina: caso ficticio con info asimétrica por sede, liderazgo rotativo, debrief con artefacto. Formato online o híbrido con jornada presencial.\n\nFormato y tiers:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/montaner/\n\n20 min si resuena.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "gra-consultores",
        "nombre": "G|R|A Consultores",
        "ciudad": "Valencia",
        "contacto": "Dirección",
        "titulo": "El Asesor Invisible",
        "subtitulo": "Una sesión lúdica para asesores de empresa familiar — el oficio donde lo que más cuesta es decirle a la familia lo que no quiere oír.",
        "pitch_lead": "G|R|A asesora a empresas familiares en sucesión, profesionalización y reinvención del modelo. El reto no es la empresa familiar del cliente — el reto es vuestro propio rol cuando la información estratégica viene cargada de afecto. Esta sesión está pensada para que los asesores reconozcan, en una mañana, los patrones que reproducen sin querer.",
        "pain_sintoma": "Asesores de empresa familiar absorben patrones del cliente y los reproducen sin verlos: deferencia, no nombrar lo incómodo, traducir conflicto en diagnóstico.",
        "pain_causa": "Larga relación con el cliente, lealtad emocional, miedo a perder el encargo si se nombra lo no nombrable.",
        "pain_no_funciona": "La supervisión entre socios. La intervisión informal. Hace falta un espacio simulado donde el rol del asesor se ponga a prueba con consecuencia visible.",
        "quote": "El asesor de empresa familiar no enseña a la familia. Le presta su voz cuando ellos no encuentran la suya.",
        "bloque1_titulo": "Caso ficticio de sucesión con información asimétrica",
        "bloque1_texto": "Roles tipo padre fundador / hijo sucesor / asesor / no familiar clave. Briefings incompletos. Decidir un escenario de sucesión sin que el asesor sepa toda la trama. Aparece qué se calla por costumbre.",
        "tier_reco": "inmersiva",
        "why_extra": "Diseñamos casos a medida de empresa familiar valenciana. No es plantilla de transformación abstracta.",
        "asunto_email": "G|R|A × Playing Camp — sesión para asesores de empresa familiar",
        "email_body": "Hola,\n\nG|R|A asesora a empresas familiares en sucesión y profesionalización. Justo ahí, el asesor absorbe patrones del cliente y los reproduce sin verlos: deferencia, no nombrar lo incómodo, traducir conflicto en diagnóstico.\n\nHe diseñado una sesión online de 2-2,5h para vuestro propio equipo de asesores: caso ficticio de sucesión, breakouts con info asimétrica, debrief con artefacto.\n\nFormato:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/gra-consultores/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "family-business-solutions",
        "nombre": "Family Business Solutions",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Asesor Invisible",
        "subtitulo": "Una sesión lúdica para el equipo que trabaja con familias empresarias — y necesita un espacio simulado para no llevarse el conflicto a casa.",
        "pitch_lead": "Family Business Solutions trabaja relevo generacional, órganos de gobierno, mediación. Trabajo de oficio emocionalmente exigente. Esta sesión es para vuestros propios asesores: un espacio simulado donde el caso es ficticio pero la fricción es real, y el debrief deja artefactos que vuelven al oficio.",
        "pain_sintoma": "Equipos de mediación familiar arrastran el conflicto del cliente al espacio interno — sin un protocolo para soltarlo o tematizarlo entre pares.",
        "pain_causa": "Exposición emocional alta, supervisión informal, ausencia de espacio simulado con caso y debrief metodológico.",
        "pain_no_funciona": "La reunión semanal. La conversación de pasillo. Hace falta una dinámica con caso, roles y artefacto compartido.",
        "quote": "El que media en lo familiar necesita, una vez al año, un espacio donde la familia sea ficticia.",
        "bloque1_titulo": "Caso ficticio de mediación familiar con información asimétrica",
        "bloque1_texto": "Roles fundador / hija / yerno / hermano no operativo / asesor externo. Briefings incompletos. Resolver un conflicto de gobernanza familiar. Aparece qué patrones del propio asesor se reproducen.",
        "tier_reco": "inmersiva",
        "why_extra": "Caso diseñado con la sensibilidad de empresa familiar española. No es plantilla anglosajona.",
        "asunto_email": "Family Business Solutions × Playing Camp — sesión para mediadores familiares",
        "email_body": "Hola,\n\nFamily Business Solutions trabaja relevo generacional, gobernanza, mediación. Oficio emocionalmente exigente: el conflicto del cliente vuelve al espacio interno sin protocolo para soltarlo entre pares.\n\nHe diseñado una sesión online de 2-2,5h para vuestro equipo: caso ficticio de mediación con info asimétrica, debrief metodológico, artefacto compartido.\n\nFormato:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/family-business-solutions/\n\n20 min si resuena.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "martinez-asociados",
        "nombre": "Martínez y Asociados",
        "ciudad": "Valencia",
        "contacto": "Dirección",
        "titulo": "El Asesor Invisible",
        "subtitulo": "Una sesión lúdica para una boutique con 20+ años en sucesión — diseñada como par profesional, no plantilla de team building.",
        "pitch_lead": "Martínez y Asociados llevan 20+ años en procesos de sucesión y profesionalización. Esa veteranía es valor — y a la vez los hábitos del oficio se sedimentan sin que nadie los cuestione. Esta sesión es la mirada de fuera con criterio metodológico, no un proveedor de animación.",
        "pain_sintoma": "Equipos con larga trayectoria tienen patrones de oficio consolidados — y los puntos ciegos van con ellos sin que nadie los nombre.",
        "pain_causa": "Costumbre de oficio, lealtad mutua entre socios, ausencia de espacio donde lo que se asume del compañero se ponga a prueba.",
        "pain_no_funciona": "La supervisión informal. La cena de socios. Hace falta una dinámica con caso, fricción medida y artefacto.",
        "quote": "20 años de oficio merecen, una vez, alguien que mire el oficio con ojos limpios.",
        "bloque1_titulo": "Caso ficticio de sucesión con información asimétrica",
        "bloque1_texto": "Roles asignados, briefings incompletos, caso de empresa familiar ficticia en sucesión. La trayectoria del oficio queda al margen y aparece lo que el grupo da por sentado.",
        "tier_reco": "esencial",
        "why_extra": "Diseño compacto y a medida. Sin plantilla. Hablamos en español neutro, sensibilidad de empresa familiar mediterránea.",
        "asunto_email": "Martínez y Asociados × Playing Camp — sesión equipo asesor sucesión",
        "email_body": "Hola,\n\nMartínez y Asociados lleva 20+ años en sucesión y profesionalización. Esa veteranía consolida patrones de oficio que rara vez se cuestionan entre socios.\n\nHe diseñado una sesión online compacta de 2h: caso ficticio de sucesión, info asimétrica, debrief metodológico. Sin slides ni plantilla.\n\nFormato:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/martinez-asociados/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "improven",
        "nombre": "Improven",
        "ciudad": "Valencia / Madrid",
        "contacto": "People & Culture",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para el equipo que alinea Estrategia · Cultura · Personas — y se merece practicarlo dentro.",
        "pitch_lead": "Improven posiciona Estrategia + Cultura + Personas como triángulo de impacto en resultado. Es triple coherencia exigente. Esta sesión es para que vuestro propio equipo directivo experimente lo que pedís a los clientes: que los tres vértices se hablen en una dinámica con consecuencia visible.",
        "pain_sintoma": "Consultoras que venden alineamiento Estrategia-Cultura-Personas tienen el reto interno de mantener esos tres vértices coherentes en su propia operación diaria.",
        "pain_causa": "Cargas comerciales fuertes, dirección operativa muy ocupada, ausencia de espacio sin agenda donde Estrategia, Cultura y Personas se sienten a la vez.",
        "pain_no_funciona": "El plan estratégico anual. La encuesta de clima. Hace falta una sesión donde los tres vértices estén forzados a hablarse.",
        "quote": "Predicar coherencia es fácil. Diseñar el espacio donde se prueba — eso es oficio.",
        "bloque1_titulo": "Caso ficticio con triple tensión Estrategia-Cultura-Personas",
        "bloque1_texto": "Roles asignados (CEO / Dir Cultura / Dir Personas / Consultor). Briefings incompletos. Decidir un movimiento estratégico que cruza los tres vértices. Aparece qué se calla.",
        "tier_reco": "inmersiva",
        "why_extra": "Cobbler's children. Vendéis alineamiento. Esta sesión es vuestro propio alineamiento, diseñado fuera del marco habitual.",
        "asunto_email": "Improven × Playing Camp — sesión Estrategia · Cultura · Personas para dentro",
        "email_body": "Hola,\n\nImproven posiciona Estrategia + Cultura + Personas como triángulo coherente. Justo eso es lo que más cuesta sostener dentro de la propia consultora cuando la carga comercial aprieta.\n\nHe diseñado una sesión online de 2-2,5h para vuestro propio equipo directivo: breakouts con info asimétrica donde los tres vértices se fuerzan a hablarse. Sin slides.\n\nFormato y opciones:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/improven/\n\n20 min si resuena.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "talentlab",
        "nombre": "Talentlab",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para la consultora que enseña talento y cambio — y vive su propia rotación interna.",
        "pitch_lead": "Talentlab vende soluciones de talento y gestión de cambio. El propio equipo interno de una consultora de talento es señal de marca: rotación, retención, cohesión. Esta sesión es para que el equipo directivo experimente, en una mañana, lo que pedís que vuestros clientes resuelvan.",
        "pain_sintoma": "Consultoras de talento que recomiendan retención y cohesión tienen la mirada del mercado encima — la rotación interna es lectura de coherencia.",
        "pain_causa": "Mercado de talento tenso, comparación con clientes propios, ausencia de espacio sin agenda donde la cohesión se diseñe en vez de asumirse.",
        "pain_no_funciona": "La encuesta de clima interna. El offsite anual. Hace falta una sesión con consecuencia visible para el grupo.",
        "quote": "El talento se queda donde vive lo que la consultora vende. Lo demás es publicidad.",
        "bloque1_titulo": "Caso ficticio de retención con información asimétrica",
        "bloque1_texto": "Roles asignados, briefings incompletos. Caso ficticio de un cliente con rotación alta. El equipo decide el approach — y descubre qué patrones reproduce internamente.",
        "tier_reco": "inmersiva",
        "why_extra": "Cobbler's children. Vendéis retención y cohesión. La sesión es vuestra prueba de marca, hecha por fuera con sensibilidad de oficio.",
        "asunto_email": "Talentlab × Playing Camp — sesión de cohesión para el equipo que vende cohesión",
        "email_body": "Hola,\n\nTalentlab vende soluciones de talento y cambio. La cohesión interna del propio equipo es señal de marca: el mercado os lee desde ahí.\n\nHe diseñado una sesión online de 2-2,5h para vuestro propio comité: caso ficticio de retención con info asimétrica, debrief metodológico, artefacto compartido. Sin slides.\n\nFormato y tres tiers:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/talentlab/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
    {
        "slug": "agc",
        "nombre": "AGC",
        "ciudad": "Madrid",
        "contacto": "Dirección",
        "titulo": "El Equipo Invisible",
        "subtitulo": "Una sesión lúdica para una boutique de transformación PYME — diseñada como par metodológico, no proveedor.",
        "pitch_lead": "AGC se posiciona como boutique de transformación organizacional centrada en ejecución para PYMEs y mercado medio. Trabajo intenso de delivery. Esta sesión es el espacio raro: el grupo directivo de AGC frente a un caso ficticio diseñado por un par metodológico, sin agenda comercial.",
        "pain_sintoma": "Consultoras boutique con foco en ejecución viven en delivery permanente — el equipo directivo rara vez para a observarse en frío.",
        "pain_causa": "Carga de proyecto, foco en cliente, ausencia de espacio sin agenda donde el propio equipo se vea en frío.",
        "pain_no_funciona": "El comité de delivery. La review trimestral. Hace falta una sesión con caso y debrief con artefacto.",
        "quote": "Las boutiques de delivery ganan con un par metodológico una vez al año, no con un proveedor de team building.",
        "bloque1_titulo": "Caso ficticio de transformación con información asimétrica",
        "bloque1_texto": "Roles asignados, briefings incompletos, caso de PYME industrial ficticia. Decidir el approach de transformación. La fricción de la información es el aprendizaje.",
        "tier_reco": "esencial",
        "why_extra": "Sesión compacta de alto retorno por hora. Sin plantilla. Diseño a medida del sector.",
        "asunto_email": "AGC × Playing Camp — sesión equipo directivo, par metodológico",
        "email_body": "Hola,\n\nAGC se posiciona como boutique de transformación con foco en ejecución para PYMEs. Carga de delivery permanente: rara vez hay espacio sin agenda donde el equipo directivo se observe en frío.\n\nHe diseñado una sesión online compacta de 2h para vuestro comité: caso ficticio, info asimétrica, debrief con artefacto. Como par metodológico, no proveedor.\n\nFormato:\nhttps://playingcamp.github.io/propuestas-pc/outreach-q3-2026/agc/\n\n20 min si encaja.\n\nCarlos Alcalá — Playing Camp",
    },
]

PRICING_TIERS = {
    "esencial": {
        "esencial_class": "opt reco",
        "inmersiva_class": "opt",
        "hibrido_class": "opt",
    },
    "inmersiva": {
        "esencial_class": "opt",
        "inmersiva_class": "opt reco",
        "hibrido_class": "opt",
    },
    "hibrido": {
        "esencial_class": "opt",
        "inmersiva_class": "opt",
        "hibrido_class": "opt reco",
    },
}

TEMPLATE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Propuesta · Playing Camp × {nombre} · {titulo}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700;900&family=Comfortaa:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{{
    --verde:#054129;
    --verde-soft:#0a5a37;
    --naranja:#F68840;
    --blanco:#FFFFFF;
    --crema:#FBF7F1;
    --tinta:#1a1a1a;
    --gris:#5a5a5a;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{background:var(--crema);color:var(--tinta);font-family:'Comfortaa',sans-serif;line-height:1.55;font-size:16px}}
  .wrap{{max-width:880px;margin:0 auto;padding:48px 40px 80px}}
  h1,h2,h3{{font-family:'Playfair Display',serif;font-weight:700;line-height:1.15;letter-spacing:-.01em}}
  h1{{font-size:54px;color:var(--verde);margin-bottom:6px}}
  h2{{font-size:30px;color:var(--verde);margin:48px 0 14px;border-bottom:2px solid var(--naranja);padding-bottom:8px;display:inline-block}}
  h3{{font-size:20px;color:var(--verde-soft);margin:24px 0 8px;font-weight:500}}
  p{{margin-bottom:12px;color:var(--tinta)}}
  strong{{color:var(--verde)}}
  em{{color:var(--naranja);font-style:normal;font-weight:500}}
  .hero{{background:var(--verde);color:var(--blanco);padding:56px 48px;border-radius:18px;margin-bottom:32px;position:relative;overflow:hidden}}
  .hero h1{{color:var(--blanco)}}
  .hero .sub{{font-family:'Playfair Display',serif;font-style:italic;font-size:22px;color:#f9d8c0;margin-top:14px;max-width:560px}}
  .hero .meta{{margin-top:32px;font-size:13px;color:#cfe3d6;letter-spacing:.04em;text-transform:uppercase}}
  .badge{{display:inline-block;background:var(--naranja);color:var(--verde);font-weight:700;padding:6px 14px;border-radius:99px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:20px}}
  .lead{{font-size:18px;color:var(--gris);max-width:680px;margin-bottom:20px}}
  .pain{{background:var(--blanco);border-left:4px solid var(--naranja);padding:22px 26px;border-radius:6px;margin:18px 0}}
  .pain p{{margin-bottom:6px}}
  ul.clean{{list-style:none;padding:0}}
  ul.clean li{{padding:10px 0 10px 28px;position:relative;border-bottom:1px dashed #e3dccf}}
  ul.clean li:last-child{{border-bottom:none}}
  ul.clean li:before{{content:"●";color:var(--naranja);position:absolute;left:8px;top:10px}}
  .timeline{{counter-reset:step;margin-top:18px}}
  .timeline .step{{background:var(--blanco);border-radius:10px;padding:18px 22px 18px 70px;margin-bottom:10px;position:relative;box-shadow:0 1px 0 rgba(0,0,0,.04)}}
  .timeline .step:before{{counter-increment:step;content:counter(step);position:absolute;left:18px;top:18px;width:36px;height:36px;border-radius:50%;background:var(--verde);color:var(--blanco);font-family:'Playfair Display',serif;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:18px}}
  .timeline .dur{{font-size:12px;color:var(--naranja);letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}}
  .timeline h4{{font-family:'Playfair Display',serif;font-size:18px;color:var(--verde);margin-bottom:4px}}
  .pricing{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}}
  .opt{{background:var(--blanco);border-radius:14px;padding:24px 22px;border:2px solid transparent;display:flex;flex-direction:column}}
  .opt.reco{{border-color:var(--naranja);box-shadow:0 8px 24px rgba(246,136,64,.15);position:relative}}
  .opt.reco:before{{content:"Recomendada";position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--naranja);color:var(--verde);font-weight:700;font-size:11px;padding:4px 12px;border-radius:99px;letter-spacing:.06em;text-transform:uppercase}}
  .opt h3{{margin-top:0;color:var(--verde)}}
  .opt .price{{font-family:'Playfair Display',serif;font-size:36px;color:var(--verde);font-weight:700;margin:8px 0 4px}}
  .opt .price small{{font-size:13px;color:var(--gris);font-weight:400;font-family:'Comfortaa',sans-serif}}
  .opt ul{{list-style:none;font-size:14px;color:var(--tinta);margin-top:12px;flex:1}}
  .opt ul li{{padding:5px 0 5px 18px;position:relative}}
  .opt ul li:before{{content:"▸";position:absolute;left:0;color:var(--naranja)}}
  .takeaways{{background:var(--verde);color:var(--blanco);padding:30px 32px;border-radius:14px;margin-top:16px}}
  .takeaways h3{{color:var(--naranja);margin-top:0}}
  .takeaways ul{{list-style:none}}
  .takeaways ul li{{padding:8px 0 8px 24px;position:relative;border-bottom:1px solid rgba(255,255,255,.12)}}
  .takeaways ul li:last-child{{border:none}}
  .takeaways ul li:before{{content:"✦";color:var(--naranja);position:absolute;left:0}}
  .why{{background:var(--blanco);padding:24px 28px;border-radius:12px;margin-top:14px}}
  .why p{{margin-bottom:10px}}
  .foot{{margin-top:60px;padding-top:24px;border-top:1px solid #e3dccf;font-size:13px;color:var(--gris);display:flex;justify-content:space-between;flex-wrap:wrap;gap:14px}}
  .foot strong{{color:var(--verde)}}
  .quote{{font-family:'Playfair Display',serif;font-style:italic;font-size:22px;color:var(--verde);border-left:3px solid var(--naranja);padding:6px 0 6px 18px;margin:24px 0;line-height:1.4}}
  @media print{{
    body{{background:var(--blanco)}}
    .wrap{{padding:18px}}
    .hero{{padding:32px}}
    h2{{font-size:24px}}
    .opt{{break-inside:avoid}}
    .pricing{{break-inside:avoid}}
    a{{color:var(--verde)}}
  }}
  @media (max-width:720px){{
    .pricing{{grid-template-columns:1fr}}
    h1{{font-size:38px}}
    .hero{{padding:36px 28px}}
    .wrap{{padding:24px 20px 60px}}
  }}
</style>
</head>
<body>
<div class="wrap">

  <section class="hero">
    <span class="badge">Propuesta confidencial</span>
    <h1>{titulo}</h1>
    <div class="sub">{subtitulo}</div>
    <div class="meta">{nombre} · {ciudad} · Atn. {contacto} · Q3 2026</div>
  </section>

  <p class="lead">{pitch_lead}</p>

  <h2>Qué leemos del reto</h2>
  <div class="pain">
    <p><strong>Síntoma observado:</strong> {pain_sintoma}</p>
    <p><strong>Causa probable:</strong> {pain_causa}</p>
    <p><strong>Lo que no funciona ya:</strong> {pain_no_funciona}</p>
  </div>

  <div class="quote">{quote}</div>

  <h2>Sesión Inicial</h2>
  <p><strong>Título de trabajo:</strong> <em>{titulo} — {subtitulo_corto}</em></p>
  <p><strong>Formato:</strong> Online sincrónica (Google Meet o Zoom), comité directivo, cámara obligatoria, breakouts rotativos.</p>

  <div class="timeline">
    <div class="step">
      <div class="dur">15 min · Apertura</div>
      <h4>El Mapa Oculto</h4>
      <p>Cada persona completa de forma anónima un mapa visual de <em>qué cree saber</em> sobre las áreas del resto. Lo proyectamos en directo. Sin reproches. Es el punto de partida visible del resto del taller.</p>
    </div>
    <div class="step">
      <div class="dur">50 min · Bloque 1 · Comunicación</div>
      <h4>{bloque1_titulo}</h4>
      <p>{bloque1_texto}</p>
    </div>
    <div class="step">
      <div class="dur">10 min · Pausa activa</div>
      <h4>Reset corporal y micro-juego</h4>
      <p>Porque dos horas online sin un descanso no las aguanta nadie.</p>
    </div>
    <div class="step">
      <div class="dur">50 min · Bloque 2 · Liderazgo</div>
      <h4>Liderar sin saberlo todo</h4>
      <p>Role-play con liderazgo rotativo. Tres escenarios donde quien decide tiene <em>menos</em> información que su equipo. Aparece lo que normalmente no se nombra: lo que cada uno guarda, por qué, y qué pasa cuando se suelta.</p>
    </div>
    <div class="step">
      <div class="dur">25 min · Debrief y aterrizaje</div>
      <h4>Patrones y compromisos</h4>
      <p>Cierre en grupo. Cada persona se lleva <strong>un hábito de comunicación implementable mañana</strong> y el grupo deja por escrito <strong>un acuerdo colectivo</strong> visible para todos.</p>
    </div>
  </div>

  <h2>Lo que se llevan</h2>
  <div class="takeaways">
    <h3>Take-aways tangibles</h3>
    <ul>
      <li>Mapa visual de puntos ciegos de información del equipo (artefacto compartido tras la sesión).</li>
      <li>1 hábito personal de comunicación, escrito, con fecha y persona testigo.</li>
      <li>Acuerdo colectivo del equipo directivo (frase corta, una sola).</li>
      <li>Kit descargable Playing Camp: 3 dinámicas breves para repetir en reuniones de dirección.</li>
    </ul>
  </div>

  <h2>Opciones de presupuesto</h2>
  <p class="lead">Tres formatos, mismo enfoque metodológico. Misma sesión nuclear; la diferencia está en preparación, materiales y seguimiento.</p>

  <div class="pricing">
    <div class="{esencial_class}">
      <h3>Esencial</h3>
      <div class="price">690 €<br><small>+ IVA · sesión única 2 h online</small></div>
      <ul>
        <li>Sesión 2 h en vivo</li>
        <li>1 reunión preparatoria 30 min</li>
        <li>Resumen post-sesión (1 página)</li>
        <li>Caso adaptado a vuestro contexto</li>
      </ul>
    </div>
    <div class="{inmersiva_class}">
      <h3>Inmersiva</h3>
      <div class="price">990 €<br><small>+ IVA · 2,5 h online + materiales + follow-up</small></div>
      <ul>
        <li>Sesión 2,5 h en vivo, todos los bloques</li>
        <li>2 reuniones preparatorias</li>
        <li>Kit descargable de 3 dinámicas</li>
        <li>Mapa visual del equipo (entregable)</li>
        <li>Follow-up 30 min a 3 semanas</li>
      </ul>
    </div>
    <div class="{hibrido_class}">
      <h3>Híbrido (siembra)</h3>
      <div class="price">desde 2.450 €<br><small>+ IVA · online + jornada presencial</small></div>
      <ul>
        <li>Todo lo de Inmersiva</li>
        <li>+ jornada team building presencial 4 h</li>
        <li>Sesión de aterrizaje a 6 semanas</li>
        <li>Acompañamiento entre fases</li>
      </ul>
    </div>
  </div>

  <h2>Por qué Playing Camp</h2>
  <div class="why">
    <p><strong>Juego como instrumento serio.</strong> No animación. El juego bien diseñado revela cómo decide y comunica un grupo bajo presión real, sin que nadie se sienta examinado.</p>
    <p><strong>Diseño a medida del reto, no plantilla.</strong> Cada dinámica se ajusta al sector y al perfil del grupo. {why_extra}</p>
    <p><strong>Confidencialidad y tono.</strong> Lo que pasa dentro de la sesión queda dentro. El facilitador no informa de individuos a dirección. Eso es lo que hace que se suelten cosas que no se sueltan en una reunión normal.</p>
  </div>

  <h2>Próximos pasos</h2>
  <ul class="clean">
    <li><strong>Presentación de la propuesta</strong> al comité.</li>
    <li>Agendamos <strong>follow-up de 20–30 min</strong> la próxima semana para resolver dudas y elegir formato.</li>
    <li>Confirmada la opción, fijamos fecha y cerramos contenidos en <strong>2-3 semanas</strong>.</li>
    <li>Facturación al cerrar fecha · 50% reserva, 50% al ejecutar.</li>
  </ul>

  <div class="foot">
    <div>
      <strong>Carlos Alcalá Marcos</strong><br>
      Playing Camp<br>
      hello@playingcamp.com · playingcamp.com
    </div>
    <div style="text-align:right">
      Propuesta válida 30 días<br>
      Q3 2026 · Documento confidencial
    </div>
  </div>

</div>
</body>
</html>
"""

def render(empresa):
    tier = empresa["tier_reco"]
    classes = PRICING_TIERS[tier]
    subt_corto = empresa["subtitulo"].split("—")[-1].strip() if "—" in empresa["subtitulo"] else empresa["subtitulo"][:80]
    return TEMPLATE.format(
        nombre=empresa["nombre"],
        ciudad=empresa["ciudad"],
        contacto=empresa["contacto"],
        titulo=empresa["titulo"],
        subtitulo=empresa["subtitulo"],
        subtitulo_corto=subt_corto,
        pitch_lead=empresa["pitch_lead"],
        pain_sintoma=empresa["pain_sintoma"],
        pain_causa=empresa["pain_causa"],
        pain_no_funciona=empresa["pain_no_funciona"],
        quote=empresa["quote"],
        bloque1_titulo=empresa["bloque1_titulo"],
        bloque1_texto=empresa["bloque1_texto"],
        why_extra=empresa["why_extra"],
        **classes,
    )

def main():
    for emp in EMPRESAS:
        folder = OUT_DIR / emp["slug"]
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(render(emp), encoding="utf-8")
        print(f"✓ {emp['slug']}/index.html")
    # emails.md
    lines = ["# Outreach Q3 2026 — Drafts emails (15 consultoras ES)\n",
             "Generado " + "2026-06-21" + " · Vertical: consultoría estratégica/transformación organizacional ES\n",
             "---\n"]
    for i, emp in enumerate(EMPRESAS, 1):
        url = f"https://playingcamp.github.io/propuestas-pc/outreach-q3-2026/{emp['slug']}/"
        lines.append(f"## {i}. {emp['nombre']} ({emp['ciudad']})\n")
        lines.append(f"**Asunto**: {emp['asunto_email']}\n")
        lines.append(f"**Propuesta**: {url}\n")
        lines.append(f"**Tier recomendado**: {emp['tier_reco']}\n\n")
        lines.append("```\n" + emp['email_body'] + "\n```\n\n---\n")
    (OUT_DIR / "emails.md").write_text("".join(lines), encoding="utf-8")
    print(f"✓ emails.md")
    # index manifest
    manifest = [{"slug": e["slug"], "nombre": e["nombre"], "ciudad": e["ciudad"],
                 "tier": e["tier_reco"], "asunto": e["asunto_email"],
                 "url": f"https://playingcamp.github.io/propuestas-pc/outreach-q3-2026/{e['slug']}/"}
                for e in EMPRESAS]
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ manifest.json")

if __name__ == "__main__":
    main()

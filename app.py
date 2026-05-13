import gradio as gr

# 🎓 Prompt système : Le "cerveau pédagogique" de LND AI
SYSTEM_PROMPT = """Tu es LND AI, un tuteur expert multi-disciplines.

Domaines d'expertise :
- 📐 Mathématiques (algèbre, analyse, probabilités, statistiques)
- 🔬 Physique (mécanique, électromagnétisme, thermodynamique, optique, quantique) ⭐ PRIORITAIRE
- ⚗️ Chimie (réactions, stoichiométrie, organique, inorganique)
- 🧬 Biologie (cellulaire, génétique, physiologie, écosystèmes)
- 💻 Informatique & Technologies IT (algorithmes, programmation, réseaux, cybersécurité, IA) ⭐ PRIORITAIRE

Règles pédagogiques STRICTES :
1. Réponds TOUJOURS en français, avec un ton clair, patient et encourageant.
2. Détecte automatiquement la matière et le niveau à partir de la question.
3. Décompose chaque réponse en étapes numérotées pour les problèmes complexes.
4. Pour les calculs : montre la démarche avant le résultat final.
5. Utilise le format LaTeX pour les formules : $E=mc^2$ ou $$...$$
6. Si la question est floue, pose une question pour préciser avant de répondre.
7. Adapte automatiquement ton niveau de détail (débutant → intermédiaire → avancé).
8. Termine chaque réponse par : "Veux-tu un exercice d'application ou que je détaille un point ?"

Structure de réponse type :
🎯 **Concept clé** : [explication courte du concept]
📝 **Développement** : [étapes détaillées numérotées]
💡 **Astuce** : [conseil pratique ou moyen mnémotechnique]
✅ **Vérification** : [si applicable, méthode pour vérifier le résultat]
"""

def repondre_chat(message, history):
    """Fonction chatbot : reçoit le message + l'historique"""
    if not message or not message.strip():
        return "👋 Bonjour ! Je suis LND AI. Pose ta question en maths, physique, chimie, biologie ou informatique."
    
    # 🔄 RÉPONSE DÉMO (pour l'instant)
    # Le SYSTEM_PROMPT ci-dessus sera utilisé quand on connectera la vraie IA
    return f"""✅ **LND AI a reçu ta question :**

📝 \"{message}\"

⏳ *Mode démo actif*

🔜 **Prochaine étape** : Je vais connecter un modèle IA gratuit qui utilisera les règles suivantes :

{SYSTEM_PROMPT}

💡 **En attendant**, teste l'interface avec :
• \"Explique la loi d'Ohm\"
• \"Dérivée de x² + 3x ?\"
• \"Comment fonctionne une boucle for ?\"
"""

# 🎨 Interface style messagerie (ChatGPT-like)
demo = gr.ChatInterface(
    fn=repondre_chat,
    title="🎓 LND AI",
    description="Professeur intelligent en sciences et technologies — Je détecte automatiquement le contexte et t'explique pas à pas.",
    examples=[
        "Explique la loi d'Ohm avec un exemple concret",
        "Comment calculer la dérivée de x² + 3x ?",
        "Qu'est-ce qu'une réaction d'oxydoréduction ?",
        "Explique le théorème de Pythagore",
        "Comment fonctionne une boucle for en Python ?",
        "Qu'est-ce que l'entropie en thermodynamique ?"
    ],
    theme="soft"  # Thème intégré directement dans ChatInterface
)

if __name__ == "__main__":
    demo.launch(share=True)

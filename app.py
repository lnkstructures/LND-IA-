import gradio as gr
import os

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

    # 🧠 Connexion au vrai cerveau IA
    try:
        from openai import OpenAI
        
        client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        
        # Construction du message avec le prompt système
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
        
        # Appel à l'IA
        response = client.chat.completions.create(
            model="qwen/qwen-2.5-7b-instruct",  # Modèle gratuit, performant, multilingue
            messages=messages,
            temperature=0.3,
            max_tokens=1000
        )
        
        reponse_ia = response.choices[0].message.content
        return reponse_ia
        
    except Exception as e:
        # Fallback si la clé n'est pas configurée
        return f"⚠️ Mode démo : clé API non configurée.\n\nTa question : \"{message}\"\n\nPour activer l'IA complète : ajoute ta clé OpenRouter dans les secrets Colab."

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

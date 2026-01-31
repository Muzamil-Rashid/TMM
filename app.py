from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# 50 Paragraphs ki List (Arre)
paragraphs_list = [
    "The quick brown fox jumps over the lazy dog. This classic sentence contains every letter of the alphabet and is often used to test typing speed and keyboard layouts. It helps users practice accuracy while becoming familiar with key placement. Regular typing practice with simple sentences builds confidence and improves muscle memory over time.",
    "Technology has revolutionized the way we communicate and work. From smartphones to cloud platforms and artificial intelligence, innovation continues to reshape daily routines. Learning how to adapt to new tools improves productivity and career growth. Typing efficiently allows professionals to interact with modern systems faster and more comfortably.",
    "Typing is an essential skill in the modern world. Students, freelancers, and professionals rely on typing for communication and productivity. Slow typing often leads to wasted time and frustration. Regular practice improves accuracy and speed, allowing users to focus more on ideas rather than struggling with the keyboard.",
    "Data is generated everywhere, from mobile applications to business transactions. Organizations depend on accurate data to make informed decisions. Poor data handling can cause incorrect conclusions. Clean and structured data helps analysts identify trends, patterns, and opportunities efficiently.",
    "Consistency is the key to mastering any skill. Small daily efforts often produce better results than irregular intense practice. Typing regularly helps build muscle memory and confidence. Over time, fingers move naturally across the keyboard without conscious effort.",
    "Problem-solving is a valuable ability in both personal and professional life. Breaking problems into smaller parts makes them easier to manage. Logical thinking and patience help find effective solutions. Strong problem-solving skills improve confidence and independence.",
    "The internet has made information easily accessible to everyone. Users can learn new skills, read articles, and watch tutorials within minutes. However, focusing on reliable sources is essential. Smart use of online resources accelerates learning and personal growth.",
    "Focus plays a major role in productivity. Distractions such as notifications reduce efficiency. Creating a calm work environment improves concentration. Even short periods of focused work can produce meaningful results and improve typing performance.",
    "Learning new skills keeps the mind active and adaptable. It opens doors to better career opportunities. Learning does not always require expensive courses; consistency and curiosity matter most. Continuous learning helps individuals stay relevant in a fast-changing world.",
    "Time management is essential for achieving goals. Planning tasks in advance reduces stress and improves results. Prioritizing important work ensures efficiency. Good time management creates balance between professional and personal life.",
    "Accuracy is as important as speed when typing. Fast typing with frequent errors reduces productivity. Building accuracy first leads to sustainable improvement. Speed naturally follows accuracy with regular practice.",
    "Clear communication avoids misunderstandings and improves collaboration. Written communication requires clarity and structure. Strong typing skills support smooth expression of ideas in emails, reports, and messages.",
    "Technology tools are designed to make work easier. Learning shortcuts and features saves time. Efficient typing allows users to interact with digital tools more effectively and comfortably.",
    "Patience is crucial when learning new skills. Progress may feel slow initially, but consistency leads to improvement. Typing speed increases gradually with regular practice and focused effort.",
    "Reading regularly improves vocabulary and comprehension. Familiarity with words improves typing speed. Reading and typing together strengthen overall language skills.",
    "Digital skills are required in almost every profession today. Typing is a foundational requirement. Strong typing skills reduce fatigue and improve confidence in professional tasks.",
    "Setting realistic goals helps maintain motivation. Gradual progress feels more sustainable. Tracking performance helps identify areas for improvement and keeps practice sessions meaningful.",
    "Work environments are becoming increasingly digital. Typing is the primary way to interact with systems. Efficient typing reduces workload and prepares individuals for future demands.",
    "Mistakes are part of the learning process. Each error provides an opportunity to improve. Understanding mistakes helps build better typing habits over time.",
    "Comfortable posture improves typing performance. Proper seating and keyboard placement reduce strain. Physical comfort directly affects speed, accuracy, and endurance.",
    "Motivation drives consistent practice. Seeing progress boosts confidence. Typing practice becomes enjoyable when learners notice improvement and growth.",
    "Short daily practice sessions are more effective than long irregular ones. Consistency strengthens muscle memory. Even ten minutes a day can lead to noticeable improvement.",
    "Accuracy-focused practice builds strong fundamentals. Correct finger placement prevents bad habits. Strong basics support long-term improvement and comfort.",
    "A calm learning environment improves performance. Reducing distractions enhances focus. Small changes in surroundings can significantly improve typing speed.",
    "Typing tests provide objective performance feedback. They help track progress and identify weaknesses. Regular testing motivates structured improvement.",
    "Language familiarity affects typing speed. Common words are typed faster. Exposure to vocabulary improves fluency and confidence.",
    "Discipline ensures consistency even when motivation drops. Scheduled practice builds strong habits. Discipline leads to long-term results.",
    "Typing remains a core skill despite technological change. Regardless of tools, typing efficiency remains valuable across platforms.",
    "Confidence grows with practice. Comfortable typing allows creativity to flow freely. Skill improvement enhances overall performance.",
    "Keyboard familiarity reduces visual dependency. Touch typing improves efficiency and focus. Repetition leads to mastery.",
    "Engaging practice content improves consistency. Variety keeps learners interested. Enjoyable practice enhances learning outcomes.",
    "Error awareness improves accuracy. Recognizing common mistakes helps correct them efficiently.",
    "Typing speed reflects practice quality. Controlled improvement leads to sustainable results.",
    "Digital communication relies heavily on typing. Efficient typing saves time and improves collaboration.",
    "Learning curves vary between individuals. Personal progress matters more than comparison.",
    "Mental focus affects typing accuracy. Short breaks refresh concentration and improve results.",
    "Repetition strengthens muscle memory. Regular typing practice leads to automation.",
    "Adaptability improves learning outcomes. Adjusting techniques enhances performance.",
    "Structured practice produces better results. Clear plans guide improvement.",
    "Accuracy builds trust in professional work. Precision strengthens credibility.",
    "Typing supports productivity and multitasking. Efficient input reduces cognitive load.",
    "Learning is a lifelong process. Continuous practice keeps skills sharp.",
    "Comfort supports endurance. Healthy habits protect long-term performance.",
    "Tracking progress motivates learners. Visible improvement encourages consistency.",
    "Typing accuracy improves writing clarity. Clean input supports better output.",
    "Focused environments enhance learning. Setup plays a vital role in performance.",
    "Dedication separates beginners from experts. Persistence leads to mastery.",
    "Small improvements compound over time. Consistency creates momentum.",
    "Typing is a gateway digital skill. Strong basics enable advanced learning.",
    "Every practice session adds value. Commitment leads to long-term success."
]

@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    # Direct list se random choice
    selected = random.choice(paragraphs_list)
    return jsonify({
        "paragraph": selected
    })

if __name__ == "__main__":
    app.run()

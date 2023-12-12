from django.shortcuts import render

# Create your views here.
def meals(request):
     meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "desc": "It helps us in various spheres of life. Healthy food does not only impact our physical health but mental health too.",
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "desc": "How healthy food makes you happy?When eating “healthy” foods as opposed to unhealthy foods, your brain responds to the nutrients you're ingesting",
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "desc": "Food can play a key role in helping you lift your mood and improve your outlook on life. While nutrition psychiatry is a relatively new field, studies are showing a "
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "desc": "Week-to-week and month-to-month, keeping your body healthy and disease-free makes good moods more likely. For example, key nutrients you get in certain foods ",
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "desc": "According to BBC Food, serotonin regulates your mood and promotes sleep, and dopamine manages feelings of motivation, attention, and emotional reward.",
            
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "desc": " When you stick to a diet of nutrient-rich foods, you're setting yourself up for fewer mood swings and an improved ability to focus. Studies have even "
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "desc":"Like an expensive car, your brain functions best when it gets only premium fuel. ",
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "desc": "Staying within your recommended daily calorie intake and eating moderately sized meals also helps you maintain a healthy weight throughout your life.",
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "desc": "Like addictive drugs, highly palatable foods trigger feel-good brain chemicals including dopamine. ",
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "desc":"It's important to note that eating specific foods isn't going to make you look noticeably younger, and that nutrition is only one aspect of aging well. ",
        }
        
        
    ]
     return render(request, 'index.html', {'meals': meals})
     
    
def sentences(request):
    word= [
        "It helps us in various spheres of life. Healthy food does not only impact our physical health but mental health too. When we intake healthy fruits and vegetables that are full of nutrients, we reduce the chances of diseases. For instance, green vegetables help us to maintain strength and vigor.",
        
        
        
    ]

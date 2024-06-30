from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .risk_assessment import RiskAssessment

@csrf_exempt
def risk_assessment_view(request):
    if request.method == 'POST':
        # Create a RiskAssessment instance
        risk_assessment = RiskAssessment()

        # Take the questionnaire
        risk_assessment.take_questionnaire()

        # Calculate the risk score
        risk_assessment.calculate_risk_score()

        # Get the risk profile
        risk_profile = risk_assessment.get_risk_profile()

        # Return the risk profile as JSON response
        return JsonResponse(risk_profile)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})


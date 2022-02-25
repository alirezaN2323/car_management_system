from django.urls import path
from .views import VehicleListAPIView, get_vehicles_with_old_owners,\
    get_vehicles_with_current_colors, get_misfeasance_cost_of_each_vehicle,\
    get_guilty_heavy_vehicles, get_general_vehicles_with_600_meters_distance


app_name = 'vehicles'

urlpatterns = [
    path('list/', VehicleListAPIView.as_view()),
    path('old_owners/', get_vehicles_with_old_owners),
    path('current_colors/', get_vehicles_with_current_colors),
    path('misfeasance_cost/', get_misfeasance_cost_of_each_vehicle),
    path('guilty_heavy_vehicles/', get_guilty_heavy_vehicles),
    path('sixty_meters_distance/', get_general_vehicles_with_600_meters_distance),

]

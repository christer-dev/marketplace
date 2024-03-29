from django.urls import path
from market import views
from market import apis

app_name = "market"

urlpatterns = [
    #API urls
    path('api/get_products/', apis.ProductViewSet.as_view({'get':'get_products'})),
    path('api/get_user_product/<int:product_id>/', apis.ProductViewSet.as_view({'get':'get_user_product'})),
    path('api/get_productDetails/<int:product_id>/', apis.ProductViewSet.as_view({'get':'get_productDetails'})),
    path('api/get_searchResult/', apis.ProductViewSet.as_view({'get':'get_searchResult'})),

    path('api/wishlist_product/<int:product_id>/', apis.WishlistViewSet.as_view({'post':'wishlist_product'})),
    path('api/get_wishlisted_products/<int:user_id>/', apis.WishlistViewSet.as_view({'get':'get_wishlisted_products'})),

    path('api/register_product/', apis.LoggedProductViewSet.as_view({'post':'register_product'})),
    path('api/modify_product/<int:product_id>/', apis.LoggedProductViewSet.as_view({'post':'modify_product'})),
    path('api/delete_product/<int:product_id>/', apis.LoggedProductViewSet.as_view({'delete':'delete_product'})),

    #Review API
    # path('api/get_comment_Object/<int:product_id>/', apis.ReviewViewSet.as_view({'get':'get_comment_Object'})),
    # path('api/get_product_comments/<int:product_id>/', apis.ReviewViewSet.as_view({'get':'get_product_comments'})),
    # path('api/add_comment/<int:product_id>/', apis.ReviewViewSet.as_view({'post':'add_comment'})),

    #Views urls
    path('registerProduct/', views.RegisterProductView.as_view(), name="registerProduct"),
    path('productDetails/<int:product_id>/', views.ProductDetailsView.as_view(), name="productDetails"),
    path('modify_product/<int:product_id>/', views.ModifyProductView.as_view(), name="modify_product"),
    path('wishlist/<int:user_id>/', views.WishlistView.as_view(), name="wishlist"),

]
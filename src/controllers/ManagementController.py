# from src.app import app
# from src.services.PageService import upload_comic_page
# from flask import jsonify, request
#
# controllerRoute = '/manage'
#
#
# @app.route('/manage/uploadPage/<int:chapter_number>/<int:page_number>', methods=['POST'])
# def upload_page(chapter_number, page_number):
#     try:
#         image_data: bytes = request.get_data()
#         upload_comic_page(chapter_number, page_number, image_data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

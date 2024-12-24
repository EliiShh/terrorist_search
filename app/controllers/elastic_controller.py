from flask import Blueprint, request, jsonify, render_template
from app.repo.elastic_repo.queris_repo import search_in_all, search_in_news, search_in_history, search_between_dates
from app.templates.maps import search_in_all_to_map


elastic_blueprint = Blueprint("elastic", __name__)


@elastic_blueprint.route('/search/keywords/<string:words>/', defaults={'limit': None})
@elastic_blueprint.route('/search/keywords/<string:words>/<int:limit>')
def route_search_in_all(words, limit):
    search_result = search_in_all("events", words)
    if len(search_result) == 0:
        return jsonify({'no results by ': words}), 404
    if limit and len(search_result) > limit:
        search_result = search_result[:limit]
    search_in_all_to_map(search_result)
    return render_template('map.html')


@elastic_blueprint.route('/search/news/<string:words>/', defaults={'limit': None})
@elastic_blueprint.route('/search/news/<string:words>/<int:limit>')
def route_search_in_news(words, limit):
    search_result = search_in_news("events", words)
    if len(search_result) == 0:
        return jsonify({'no results by ': words}), 404
    if limit and len(search_result) > limit:
        search_result = search_result[:limit]
    search_in_all_to_map(search_result)
    return render_template('map.html')


@elastic_blueprint.route('/search/historic/<string:words>/', defaults={'limit': None})
@elastic_blueprint.route('/search/historic/<string:words>/<int:limit>')
def route_search_in_history(words, limit):
    search_result = search_in_history("events", words)
    if len(search_result) == 0:
        return jsonify({'no results by ': words}), 404
    if limit and len(search_result) > limit:
        search_result = search_result[:limit]
    search_in_all_to_map(search_result)
    return render_template('map.html')

@elastic_blueprint.route('/search/combined/<string:words>/<string:start_date>/<string:end_date>', defaults={'limit': None})
@elastic_blueprint.route('/search/combined/<string:words>/<string:start_date>/<string:end_date>/<int:limit>')
def route_search_between_dates(words, limit, start_date, end_date):
    search_result = search_between_dates("events", words, start_date, end_date)
    if len(search_result) == 0:
        return jsonify({'no results by ': words}), 404
    if limit and len(search_result) > limit:
        search_result = search_result[:limit]
    search_in_all_to_map(search_result)
    return render_template('map.html')

# coding: utf-8

import urllib

from vimeo import exceptions


def _get_querystring(filter_dict):
    query_pairs = [(str(k), str(v)) for k, v in filter_dict.iteritems()]
    return urllib.urlencode(query_pairs)


class VimeoClientMethodMixin(object):
    def check_response(self, response, success_code, error_codes):

        if response.status_code == success_code:
            # HTTP SUCCESS CODE
            self.logger.debug('Successful API call')
            return response

        if response.status_code in error_codes:
            # HTTP KNOWN ERROR CODE
            exception_name = 'HTTPError{error_code}Exception'.format(error_code=response.status_code)
            raise getattr(exceptions, exception_name)(response=response)
        else:
            # HTTP UNKNOWN ERROR CODE
            raise exceptions.UnexpectedHTTPErrorException(response=response)

    # ---===   HTTP METHODS   ===--- #
    def get_method(self, uri, filter_dict=None, success_code=200, error_codes=list()):
        uri_to_call = '{}?{}'.format(uri, _get_querystring(filter_dict or dict())) if filter_dict else uri
        self.logger.debug('GET: {uri_to_call}'.format(uri_to_call=uri_to_call))
        response = self.get(uri_to_call)
        return self.check_response(response, success_code, error_codes)

    def post_method(self, uri, data, success_code=200, error_codes=list()):
        self.logger.debug('POST: {uri}'.format(uri=uri))
        response = self.post(uri, data=data)
        return self.check_response(response, success_code, error_codes)

    def patch_method(self, uri, data, success_code=200, error_codes=list()):
        self.logger.debug('PATCH: {uri}'.format(uri=uri))
        response = self.patch(uri, data=data)
        return self.check_response(response, success_code, error_codes)

    def put_method(self, uri, success_code=200, error_codes=list()):
        self.logger.debug('PUT: {uri}'.format(uri=uri))
        response = self.put(uri)
        return self.check_response(response, success_code, error_codes)

    def delete_method(self, uri, success_code=200, error_codes=list()):
        self.logger.debug('DELETE: {uri}'.format(uri=uri))
        response = self.delete(uri)
        return self.check_response(response, success_code, error_codes)

    # ---===   INFORMATION   ===--- #
    def read_user(self):
        """
        Get a user.
        :return: response
        """
        uri = '/me'
        return self.get_method(uri)

    def update_user(self, data=None):
        """
        Edit a single user.
        :return: response
        """
        uri = '/me'
        return self.patch_method(uri, data=data or dict())

    # ---===   ALBUMS   ===--- #
    def read_albums(self, filter_dict=None):
        """
        Get a list of a user's Albums.
        :return: response
        """
        uri = '/me/albums'
        return self.get_method(uri, filter_dict=filter_dict or dict(), error_codes=[400])

    def create_album(self, name, description, privacy=None, password=None, sort=None):
        """
        Create an Album.
        :param name: The Album title
        :param description: The Album description
        :param privacy: The Album's privacy level (anybody, password)
        :param password: Required if privacy=password. The Album's password
        :param sort: The default sort order of an Album's videos (arranged, newest, oldest, plays, comments, likes,
            added_first, added_last, alphabetical)
        :return: response
        """
        uri = "/me/albums"
        data = dict(name=name, description=description, privacy=privacy, password=password, sort=sort)
        return self.post_method(uri, data=data, success_code=201, error_codes=[400, 401, 403])

    def read_album(self, album_id):
        """
        Get info on an Album.
        :param album_id
        :return: response
        """
        uri = "/me/albums/{album_id}".format(album_id=album_id)
        return self.get_method(uri, error_codes=[404])

    def update_album(self, album_id, data):
        """
        Get info on an Album.
        :param album_id
        :param data
        :return: response
        """
        uri = "/me/albums/{album_id}".format(album_id=album_id)
        return self.patch_method(uri, data, error_codes=[400, 403])

    def delete_album(self, album_id):
        """
        Delete an Album.
        :param album_id
        :return: response
        """
        uri = "/me/albums/{album_id}".format(album_id=album_id)
        return self.delete_method(uri, success_code=204, error_codes=[403, 404])

    def read_album_videos(self, album_id, filter_dict=None):
        """
        Get the list of videos in an Album.
        :param filter_dict: filters
        :param album_id
        :return: response
        """
        uri = "/me/albums/{album_id}/videos".format(album_id=album_id)
        return self.get_method(uri, error_codes=[404], filter_dict=filter_dict or dict())

    def read_video_from_album(self, album_id, video_id):
        """
        Check if an Album contains a video.
        :param album_id
        :param video_id
        :return: response
        """
        uri = "/me/albums/{album_id}/videos/{video_id}". format(
            album_id=album_id, video_id=video_id
        )
        return self.get_method(uri, error_codes=[404])

    def add_video_to_album(self, album_id, video_id):
        """
        Add a video to an Album.
        :param album_id
        :param video_id
        :return: response
        """
        uri = "/me/albums/{album_id}/videos/{video_id}".format(album_id=album_id, video_id=video_id)
        return self.put_method(uri, success_code=204, error_codes=[403, 404])

    def remove_video_from_album(self, album_id, video_id):
        """
        Remove a video from an Album.
        :param album_id
        :param video_id
        :return: response
        """
        uri = "/me/albums/{album_id}/videos/{video_id}".format(album_id=album_id, video_id=video_id)
        return self.delete_method(uri, success_code=204, error_codes=[403, 404])

    # ---===   APPEARANCES   ===--- #
    def read_appearance_videos(self, filter_dict=None):
        """
        Get all videos that a user appears in.
        :return: response
        """
        uri = "/me/appearances"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    # ---===   CHANNELS   ===--- #
    def read_channels(self, filter_dict=None):
        """
        return a list of the Channels a user follows.
        :return: response
        """
        uri = "/me/channels"
        return self.get_method(uri, error_codes=[304], filter_dict=filter_dict or dict())

    def create_channel(self):
        """
        create channel
        :return: response
        """
        uri = "/me/channels"
        return self.post_method(uri)

    def read_channel(self, channel_id):
        """
        Check if a user follows a Channel.
        :param channel_id
        :return: response
        """
        uri = "/me/channels/{channel_id}".format(channel_id=channel_id)
        return self.get_method(uri, success_code=204, error_codes=[404])

    def subscribe_channel(self, channel_id):
        """
        Subscribe to a Channel.
        :param channel_id
        :return: response
        """
        uri = "/me/channels/{channel_id}".format(channel_id=channel_id)
        return self.put_method(uri, success_code=204)

    def unsubscribe_channel(self, channel_id):
        """
        Unsubscribe from a Channel.
        :param channel_id
        :return: response
        """
        uri = "/me/channels/{channel_id}".format(channel_id=channel_id)
        return self.delete_method(uri, success_code=204, error_codes=[403])

    def read_categories(self, filter_dict=None):
        """
        Get a list of the Categories a user follows.
        :return: response
        """
        uri = "/me/categories"
        return self.get_method(uri, error_codes=[403], filter_dict=filter_dict or dict())

    def read_category(self, category_id):
        """
        Check if a user follows a Category.
        :param category_id
        :return: response
        """
        uri = "/me/categories/{category_id}".format(category_id=category_id)
        return self.get_method(uri, success_code=204)

    def subscribe_category(self, category_id):
        """
        Subscribe to a Category.
        :param category_id
        :return: response
        """
        uri = "/me/categories/{category_id}".format(category_id=category_id)
        return self.put_method(uri, success_code=204)

    def unsubscribe_category(self, category_id):
        """
        Unsubscribe from a Category.
        :param category_id
        :return: response
        """
        uri = "/me/categories/{category_id}".format(category_id=category_id)
        return self.delete_method(uri, success_code=204)

    # ---===   GROUPS   ===--- #
    def read_groups(self, filter_dict=None):
        """
        Get a list of the Groups a user has joined.
        :return: response
        """
        uri = "/me/groups"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def read_group(self, group_id):
        """
        Check if a user has joined a Group
        :return: response
        """
        uri = "/me/groups/{group_id}".format(group_id=group_id)
        return self.get_method(uri, success_code=204, error_codes=[404])

    def join_group(self, group_id):
        """
        Join a Group.
        :param group_id
        :return: response
        """
        uri = "/me/groups/{group_id}".format(group_id=group_id)
        return self.put_method(uri, success_code=204, error_codes=[403])

    def leave_group(self, group_id):
        """
        Leave a Group.
        :param group_id
        :return: response
        """
        uri = "/me/groups/{group_id}".format(group_id=group_id)
        return self.delete_method(uri, success_code=204, error_codes=[403])

    # ---===   FEED   ===--- #
    def read_feed_videos(self, filter_dict=None):
        """
        Get a list of the videos in your feed.
        :return: response
        """
        uri = "/me/feed"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    # ---===   FOLLOWERS   ===--- #
    def read_followers(self, filter_dict=None):
        """
        Get a list of the user's followers.
        :return: response
        """
        uri = "/me/followers"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    # ---===   FOLLOWING   ===--- #
    def read_following_users(self, filter_dict=None):
        """
        Get a list of the users that a user is following.
        :return: response
        """
        uri = "/me/following"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def read_follow_user(self, follow_user_id):
        """
        Check if a user follows another user.
        :return: response
        """
        uri = "/me/following/{follow_user_id}".format(follow_user_id=follow_user_id)
        return self.get_method(uri, success_code=204, error_codes=[404])

    def follow_user(self, follow_user_id):
        """
        Follow a user.
        :param follow_user_id
        :return: response
        """
        uri = "/me/following/{follow_user_id}".format(follow_user_id=follow_user_id)
        return self.put_method(uri, success_code=204, error_codes=[404])

    def unfollow_user(self, follow_user_id):
        """
        Unfollow a user.
        :param follow_user_id
        :return: response
        """
        uri = "/me/following/{follow_user_id}".format(follow_user_id=follow_user_id)
        return self.delete_method(uri, success_code=204)

    # ---===   LIKES   ===--- #
    def read_liked_videos(self, filter_dict=None):
        """
        Get a list of videos that a user likes.
        :return: response
        """
        uri = "/me/likes"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def read_liked_video(self, video_id):
        """
        Check if a user likes a video.
        :return: response
        """
        uri = "/me/likes/{video_id}".format(video_id=video_id)
        return self.get_method(uri, success_code=204, error_codes=[404])

    def like_video(self, video_id):
        """
        Like a video.
        :param video_id
        :return: response
        """
        uri = "/me/likes/{video_id}".format(video_id=video_id)
        return self.put_method(uri, success_code=204, error_codes=[400, 403])

    def unlike_video(self, video_id):
        """
        Unlike a video.
        :param video_id
        :return: response
        """
        uri = "/me/likes/{video_id}".format(video_id=video_id)
        return self.delete_method(uri, success_code=204, error_codes=[400, 403])

    # ---===   PICTURES   ===--- #
    def read_pictures(self):
        """
        Get a list of this user's portrait images.
        :return: response
        """
        uri = "/me/pictures"
        return self.get_method(uri)

    def create_pictures(self, data):
        """
        Create a new picture resource.
        :return: response
        """
        uri = "/me/pictures"
        return self.post_method(uri, data, success_code=201)

    def read_portrait(self, portraitset_id):
        """
        Check if a user has a portrait.
        :param portraitset_id
        :return: response
        """
        uri = "/me/pictures/{portraitset_id}".format(portraitset_id=portraitset_id)
        return self.get_method(uri)

    def remove_portrait(self, portraitset_id):
        """
        Remove a portrait from your portrait list.
        :param portraitset_id
        :return: response
        """
        uri = "/me/pictures/{portraitset_id}".format(portraitset_id=portraitset_id)
        return self.get_method(uri, success_code=204)

    # ---===   PORTFOLIOS   ===--- #
    def read_portfolios(self, filter_dict=None):
        """
        Get a list of Portfolios created by a user.
        :return: response
        """
        uri = "me/portfolios"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def read_portfolio(self, portfolio_id):
        """
        Get a Portfolio.
        :param portfolio_id
        :return: response
        """
        uri = "/me/portfolios/{portfolio_id}".format(portfolio_id=portfolio_id)
        return self.get_method(uri)

    def read_portfolio_videos(self, portfolio_id, filter_dict=None):
        """
        Get the videos in this Portfolio.
        :return:
        """
        uri = "/me/portfolios/{portfolio_id}/videos".format(portfolio_id=portfolio_id)
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def read_video_from_portfolio(self, portfolio_id, video_id):
        """
        Check if a Portfolio contains a video.
        :param portfolio_id
        :param video_id
        :return: RESPONSE
        """
        uri = "/me/portfolios/{portfolio_id}/videos/{video_id}".format(
            portfolio_id=portfolio_id, video_id=video_id
        )
        return self.get_method(uri, success_code=204, error_codes=[404])

    def add_video_to_portfolio(self, portfolio_id, video_id):
        """
        Add a video to the Portfolio.
        :param portfolio_id
        :param video_id
        :return: RESPONSE
        """
        uri = "/me/portfolios/{portfolio_id}/videos/{video_id}".format(
            portfolio_id=portfolio_id, video_id=video_id
        )
        return self.put_method(uri, success_code=204, error_codes=[404])

    def remove_video_from_portfolio(self, portfolio_id, video_id):
        """
        Remove a video from the Portfolio.
        :param portfolio_id
        :param video_id
        :return: RESPONSE
        """
        uri = "/me/portfolios/{portfolio_id}/videos/{video_id}".format(
            portfolio_id=portfolio_id, video_id=video_id
        )
        return self.delete_method(uri, success_code=204, error_codes=[404])

    # ---===   WATCHED VIDEO   ===--- #
    def get_watched_videos(self):
        """
        View all videos you have watched
        :return: response
        """
        uri = "/me/watched/videos"
        return self.get_method(uri)

    def clear_all_watch_history(self):
        """
        Clear your entire watch history.
        :return: response
        """
        uri = "/me/watched/videos"
        return self.delete_method(uri)

    def remove_video_from_watch_history(self, video_id):
        """
        Remove a video from your watch history
        :return: response
        """
        uri = "/me/watched/videos/{video_id}".format(video_id=video_id)
        return self.delete_method(uri, success_code=204)

    # ---===   PRESETS   ===--- #
    def get_presets(self, filter_dict=None):
        """
        Get all presets created by the authenticated user.
        :return: response
        """
        uri = "/me/presets"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def get_preset(self, preset_id):
        """
        Get a preset.
        :param preset_id
        :return: response
        """
        uri = "/me/presets/{preset_id}".format(preset_id=preset_id)
        return self.get_method(uri)

    def update_preset(self, preset_id, data):
        """
        Edit a preset.
        :param preset_id
        :param data
        :return: response
        """
        uri = "/me/presets/{preset_id}".format(preset_id=preset_id)
        return self.patch_method(uri, data, error_codes=[400, 404])

    def get_preset_videos(self, preset_id):
        """
        Get videos that have the provided preset.
        :param preset_id
        :return: response
        """
        uri = "/me/presets/{preset_id}/videos".format(preset_id=preset_id)
        return self.get_method(uri)

    # ---===   VIDEOS   ===--- #
    def get_videos(self, filter_dict=None):
        """
        Get a list of videos uploaded by a user.
        :return: response
        """
        uri = "/me/videos"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def post_video(self, redirect_url, upload_url):
        """
        Begin the video upload process.
        :param redirect_url: app redirect URL
        :param upload_url: this URL must be valid for at least 24 hours
        :return: response
        """
        uri = "/me/videos"
        data = dict(type='POST', redirect_url=redirect_url, upload_url=upload_url)
        return self.post_method(uri, data=data, success_code=201, error_codes=[403])

    def get_video(self, video_id):
        """
        return video
        :param video_id:
        :return: response
        """
        uri = "/me/videos/{video_id}".format(video_id=video_id)

        return self.get_method(uri, error_codes=[404])

    # ---===   WATCH LATER   ===--- #
    def read_watchlaters(self, filter_dict=None):
        """
        Get the authenticated user's Watch Later queue.
        :return: response
        """
        uri = "/me/watchlater"
        return self.get_method(uri, filter_dict=filter_dict or dict())

    def read_watchlater(self, video_id):
        """
        Check if a video is in the authenticated user's Watch Later queue.
        :return: response
        """
        uri = "/me/watchlater/{video_id}".format(video_id=video_id)
        return self.get_method(uri, success_code=204, error_codes=[404])

    def add_watchlater(self, video_id):
        """
        Add a video to the authenticated user's watch later list.
        :return: response
        """
        uri = "/me/watchlater/{video_id}".format(video_id=video_id)
        return self.put_method(uri, success_code=204)

    def remove_watchlater(self, video_id):
        """
        Remove a video from your watch later list.
        :return: response
        """
        uri = "/me/watchlater/{video_id}".format(video_id=video_id)
        return self.delete_method(uri, success_code=204)

    # ---===   ON DEMAND   ===--- #
    def read_ondemand_pages(self, filter_dict):
        """
        Get a user's On Demand pages
        :return: response
        """
        uri = "/me/ondemand/pages"
        return self.get_method(uri, filter_dict=filter_dict or dict(), error_codes=[404])

    def add_ondemand_pages(self, data):
        """
        Create an On Demand page.
        :return: response
        """
        uri = "/me/ondemand/pages"
        return self.post_method(uri, data=data)

    # ---===   ON DEMAND PURCHASES   ===--- #
    def read_ondemand_purchases(self, filter_dict):
        """
        Get a users On Demand purchases and rentals.
        :return: response
        """
        uri = '/me/ondemand/purchases'
        return self.get_method(uri, filter_dict=filter_dict or dict(), error_codes=[400, 403])

    def read_ondemand_purchase(self, ondemand_id):
        """
        Check if an On Demand page is in your purchases.
        :return: response
        """
        uri = '/me/ondemand/purchases{ondemand_id}'.format(ondemand_id=ondemand_id)
        return self.get_method(uri, error_codes=[403, 404])

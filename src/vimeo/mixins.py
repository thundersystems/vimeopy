# coding: utf-8

import urllib

from vimeo import exceptions


def _get_querystring(filter_dict):
    query_pairs = [(str(k), str(v)) for k, v in filter_dict.iteritems()]
    return urllib.urlencode(query_pairs)


class VimeoClientMethodMixin(object):
    def get_method(self, uri, valid_codes, filter_dict=None):
        response = self.get('{}?{}'.format(
            uri, _get_querystring(filter_dict or dict())
        ))
        if response.status_code in valid_codes:
            return response
        raise exceptions.BadRequestException(
            status_code=response.status_code, error_msg=response.json(), url=response.url
        )

    def post_method(self, uri, valid_codes, data):
        response = self.post(uri, data=data)
        if response.status_code in valid_codes:
            return response
        raise exceptions.BadRequestException(
            status_code=response.status_code, error_msg=response.json(), url=response.url
        )

    def patch_method(self, uri, valid_codes, data):
        response = self.patch(uri, data=data)
        if response.status_code in valid_codes:
            return response
        raise exceptions.BadRequestException(
            status_code=response.status_code, error_msg=response.json(), url=response.url
        )

    def put_method(self, uri, valid_codes):
        response = self.put(uri)
        if response.status_code in valid_codes:
            return response
        raise exceptions.BadRequestException(
            status_code=response.status_code, error_msg=response.json(), url=response.url
        )

    def delete_method(self, uri, valid_codes):
        response = self.delete(uri)
        if response.status_code in valid_codes:
            return response
        raise exceptions.BadRequestException(
            status_code=response.status_code, error_msg=response.json(), url=response.url
        )

    # ---===   CURRENT USER   ===--- #
    def read_user(self):
        """
        return user
        :return: response
        """
        uri = '/me'
        return self.get_method(uri, valid_codes=[200])

    def update_user(self, data=None):
        """
        update user
        :return: response
        """
        uri = '/me'
        return self.patch_method(uri, valid_codes=[200], data=data or dict())

    # ---===   ALBUMS   ===--- #
    def read_albums(self):
        """
        return a list of a user's Albums.
        :return: response
        """
        uri = '/me/albums'
        return self.get_method(uri, valid_codes=[200])

    def read_album(self, album_id):
        """
        return info on an Album.
        :param album_id
        :return: response
        """
        uri = "/me/albums/{album_id}".format(album_id=album_id)
        return self.get_method(uri, valid_codes=[200])

    def read_album_videos(self, album_id, filter_dict=None):
        """
        return the list of videos in an Album
        :param album_id
        :return: response
        """
        uri = "/me/albums/{album_id}/videos".format(album_id=album_id)
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def read_video_from_album(self, album_id, video_id):
        """
        check if an Album contains a video
        :param album_id
        :param video_id
        :return: response
        """
        uri = "/me/albums/{album_id}/videos/{video_id}". format(
            album_id=album_id, video_id=video_id
        )
        return self.get_method(uri, valid_codes=[200])

    def create_album(self, name, description, privacy=None, password=None, sort=None):
        """
        post a new album
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
        return self.post_method(uri, valid_codes=[200, 201], data=data)

    def update_album(self, album_id, name=None, description=None, privacy=None, password=None, sort=None):
        """
        update album
        :param album_id
        :param name: The Album title
        :param description: The Album description
        :param privacy: The Album's privacy level (anybody, password)
        :param password: Required if privacy=password. The Album's password
        :param sort: The default sort order of an Album's videos (arranged, newest, oldest, plays, comments, likes,
            added_first, added_last, alphabetical)
        :return: response
        """
        uri = "/me/albums/{album_id}".format(album_id=album_id)
        data = dict(name=name, description=description, privacy=privacy, password=password, sort=sort)
        return self.patch_method(uri, valid_codes=[200], data=data)

    def add_video_to_album(self, album_id, video_id):
        """
        add video to album
        :param album_id
        :param video_id
        :return: response
        """
        uri = "/me/albums/{album_id}videos/{video_id}".format(album_id=album_id, video_id=video_id)
        return self.put_method(uri, valid_codes=[200])

    def delete_album(self, album_id):
        """
        delete an album
        :param album_id
        :return: response
        """
        uri = "/me/albums/{album_id}".format(album_id)
        return self.delete_method(uri, valid_codes=[200])

    # ---===   APPEARANCES   ===--- #
    def read_appearance_videos(self, filter_dict=None):
        """
        return all videos that a user appears in
        :return: response
        """
        uri = "/me/appearances"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    # ---===   CHANNELS   ===--- #
    def read_channels(self, filter_dict=None):
        """
        return a list of the Channels a user follows.
        :return: response
        """
        uri = "/me/channels"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def create_channel(self):
        """
        create channel
        :return: response
        """
        uri = "/me/channels"
        return self.post_method(uri, valid_codes=[200])

    def read_channel(self, channel_id):
        """
        check if a user follows a Channel
        :param channel_id
        :return: response
        """
        uri = "/me/channels/{channel_id}".format(channel_id=channel_id)
        return self.get_method(uri, valid_codes=[200])

    def subscribe_channel(self, channel_id):
        """
        subscribe ro channel
        :param channel_id
        :return: response
        """
        uri = "/me/channels/{channel_id}".format(channel_id=channel_id)
        return self.put_method(uri, valid_codes=[200])

    def unsubscribe_channel(self, channel_id):
        """
        unsubscribe ro channel
        :param channel_id
        :return: response
        """
        uri = "/me/channels/{channel_id}".format(channel_id=channel_id)
        return self.delete_method(uri, valid_codes=[200])

    # ---===   CATEGORIES   ===--- #

    # ---===   GROUPS   ===--- #
    def read_groups(self):
        """
        return a list of the Groups a user has joined
        :return: response
        """
        uri = "/me/groups"
        return self.get_method(uri, valid_codes=[200])

    def read_group(self, group_id):
        """
        check if a user has joined a Group
        :return: response
        """
        uri = "/me/groups/{group_id}".format(group_id=group_id)
        return self.get_method(uri, valid_codes=[200])

    def join_group(self, group_id):
        """
        join to group
        :param group_id
        :return: response
        """
        uri = "/me/groups/{group_id}".format(group_id=group_id)
        return self.put_method(uri, valid_codes=[200])

    def leave_group(self, group_id):
        """
        leave group
        :param group_id
        :return: response
        """
        uri = "/me/groups/{group_id}".format(group_id=group_id)
        return self.delete_method(uri, valid_codes=[200])

    # ---===   FEED   ===--- #
    def read_feed_videos(self, filter_dict=None):
        """
        return a list of the videos in your feed
        :return: response
        """
        uri = "/me/feed"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    # ---===   FOLLOWERS   ===--- #
    def read_followers(self, filter_dict=None):
        """
        return a list of the user's followers
        :return: response
        """
        uri = "/me/followers"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def read_following_users(self, filter_dict=None):
        """
        return a list of the users that a user is following
        :return: response
        """
        uri = "/me/following"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def read_follow_user(self, follow_user_id):
        """
        check if a user follows another user.
        :return: response
        """
        uri = "/me/following/{follow_user_id}".format(follow_user_id=follow_user_id)
        return self.get_method(uri, valid_codes=[200])

    def follow_user(self, follow_user_id):
        """
        follow user
        :param follow_user_id
        :return: response
        """
        uri = "/me/following/{follow_user_id}".format(follow_user_id)
        return self.put_method(uri, valid_codes=[200])

    def unfollow_user(self, follow_user_id):
        """
        unfollow user
        :param follow_user_id
        :return: response
        """
        uri = "/me/following/{follow_user_id}".format(follow_user_id)
        return self.delete_method(uri, valid_codes=[200])

    # ---===   LIKES   ===--- #
    def read_liked_videos(self, filter_dict=None):
        """
        return a list of videos that a user likes
        :return: response
        """
        uri = "/me/likes"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def read_liked_video(self, video_id):
        """
        check like a video
        :return: response
        """
        uri = "/me/likes/{video_id}".format(video_id=video_id)
        return self.get_method(uri, valid_codes=[200])

    def like_video(self, video_id):
        """
        like video
        :param video_id
        :return: response
        """
        uri = "/me/likes/{video_id}".format(video_id=video_id)
        return self.put_method(uri, valid_codes=[200])

    def unlike_video(self, video_id):
        """
        unlike video
        :param video_id
        :return: response
        """
        uri = "/me/likes/{video_id}".format(video_id=video_id)
        return self.delete_method(uri, valid_codes=[200])

    # ---===   PICTURES   ===--- #
    def read_pictures(self):
        """
        return a list of this user's portrait images
        :return: response
        """
        uri = "/me/pictures"
        return self.get_method(uri, valid_codes=[200])

    def read_portrait(self, portraitset_id):
        """
        check if a user has a portrait
        :param portraitset_id
        :return: response
        """
        uri = "/me/pictures/{portraitset_id}".format(portraitset_id=portraitset_id)
        return self.get_method(uri, valid_codes=[200])

    # ---===   PORTFOLIOS   ===--- #
    def read_portfolios(self, filter_dict=None):
        """
        return a list of Portfolios created by a user
        :return: response
        """
        uri = "me/portfolios"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def read_portfolio(self, portfolio_id):
        """
        return portfolio
        :param portfolio_id
        :return: response
        """
        uri = "/me/portfolios/{portfolio_id}".format(portfolio_id=portfolio_id)
        return self.get_method(uri, valid_codes=[200])

    def read_portfolio_videos(self, portfolio_id, filter_dict=None):
        """
        return a list of portfolio videos
        :return:
        """
        uri = "/me/portfolios/{portfolio_id}/videos".format(portfolio_id)
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def read_video_from_portfolio(self, portfolio_id, video_id):
        """
        get video from portfolio
        :param portfolio_id
        :param video_id
        :return: RESPONSE
        """
        uri = "/me/portfolios/{portfolio_id}/videos/{video_id}".format(
            portfolio_id=portfolio_id, video_id=video_id
        )
        return self.get_method(uri, valid_codes=[200])

    def add_video_to_portfolio(self, portfolio_id, video_id):
        """
        add video to portfolio
        :param portfolio_id
        :param video_id
        :return: RESPONSE
        """
        uri = "/me/portfolios/{portfolio_id}/videos/{video_id}".format(
            portfolio_id=portfolio_id, video_id=video_id
        )
        return self.put_method(uri, valid_codes=[200])

    def remove_video_from_portfolio(self, portfolio_id, video_id):
        """
        remove video from portfolio
        :param portfolio_id
        :param video_id
        :return: RESPONSE
        """
        uri = "/me/portfolios/{portfolio_id}/videos/{video_id}".format(
            portfolio_id=portfolio_id, video_id=video_id
        )
        return self.delete_method(uri, valid_codes=[200])

    # ---===   WATCHED VIDEO   ===--- #
    def get_watched_videos(self):
        """
        return a list of watched videos
        :return: response
        """
        uri = "/me/watched/videos"
        return self.get_method(uri, valid_codes=[200])

    def clear_all_watch_history(self):
        """
        clear all watch history
        :return: response
        """
        uri = "/me/watched/videos"
        return self.delete_method(uri, valid_codes=[200])

    def remove_video_from_watch_history(self, video_id):
        """
        remove video from watch history
        :return: response
        """
        uri = "/me/watched/videos/{video_id}".format(video_id)
        return self.delete_method(uri, valid_codes=[200])

    # ---===   PRESETS   ===--- #
    def get_presets(self, filter_dict=None):
        """
        return a list of presets
        :return: response
        """
        uri = "/me/presets"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def get_preset(self, preset_id):
        """
        return preset
        :param preset_id
        :return: response
        """
        uri = "/me/presets/{preset_id}".format(preset_id=preset_id)
        return self.get_method(uri, valid_codes=[200])

    def update_preset(self, preset_id):
        """
        update preset
        :param preset_id
        :return: response
        """
        uri = "/me/presets/{preset_id}".format(preset_id=preset_id)
        return self.patch_method(uri, valid_codes=[200])

    def get_preset_videos(self, preset_id):
        """
        Get videos that have the provided preset.
        :param preset_id
        :return: response
        """
        uri = "/me/presets/{preset_id}/videos".format(preset_id=preset_id)
        return self.get_method(uri, valid_codes=[200])

    # ---===   VIDEOS   ===--- #
    def get_videos(self, filter_dict=None):
        """
        return a list of videos
        :return: response
        """
        uri = "/me/videos"
        return self.get_method(uri, valid_codes=[200], filter_dict=filter_dict or dict())

    def get_video(self, video_id):
        """
        return video
        :param video_id:
        :return: response
        """
        uri = "/me/videos/{video_id}".format(video_id=video_id)

        return self.get_method(uri, valid_codes=[200])

    def post_video(self, redirect_url, upload_url):
        """
        upload video from upload url
        :param redirect_url: app redirect URL
        :param upload_url: this URL must be valid for at least 24 hours
        :return: response
        """
        uri = "/me/videos"
        data = dict(type='POST', redirect_url=redirect_url, upload_url=upload_url)
        return self.post_method(uri, valid_codes=[200], data=data)

from website.models import UserDetails, Auction, Bid
from django.utils import timezone
from datetime import datetime, timedelta

from decimal import Decimal


def increase_bid(user, auction):
    """
    Removes €1.0 from user.
    Creates a Bid record
    Increases the auction's number of bids

    Parameters
    ----------
    auction : class 'website.models.Auction'
    """
    # Fetch the UserDetails associated with the user
    userDetails = UserDetails.objects.get(user_id=user.id)
    # Deduct 1.0 from the user's balance
    userDetails.balance -= Decimal('1.0')  # Use Decimal object for consistency
    userDetails.save()  # Save the updated balance to the database

    # Create a new Bid record
    bid = Bid.objects.create(user_id=user, auction_id=auction, bid_time=timezone.now())

    # Increase the auction's number of bids
    auction.number_of_bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=5)
    auction.save()


def remaining_time(auction):
    """
    Calculates the auction's remaining time
    in minutes and seconds and converts them 
    into a string.
    
    Parameters
    ----------
    auction : class 'website.models.Auction
    
    Returns
    -------
    
    time_left : str
        string representation of remaining time in
        minutes and seconds.
    expired : int
        if the value is less than zero then the auction ended.
    
    """
    time_left = auction.time_ending - timezone.now()
    days, seconds = time_left.days, time_left.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_left = str(minutes) + "m " + str(seconds) + "s"
    expired = days

    return time_left, expired

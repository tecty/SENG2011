class Post{
  ghost var Bidding: bool;
  ghost var Deal: bool;
  ghost var Finished: bool;
  ghost var Canceled: bool;

  predicate Valid()
  reads this 
  {
    ( Bidding && !Deal && !Finished && !Canceled) || 
    (!Bidding &&  Deal && !Finished && !Canceled) || 
    (!Bidding && !Deal &&  Finished && !Canceled) || 
    (!Bidding && !Deal && !Finished &&  Canceled) 
  }


  constructor()
  ensures Valid();
  ensures Bidding == true;
  {
    // start the post 
    Bidding  := true;
    Deal     := false;
    Finished := false;
    Canceled := false;
  }

  // choose the bid 
  // checkout the deal state 
  method ChooseBid()
  modifies this;
  requires Valid();ensures Valid();
  requires Bidding == true;
  ensures Deal == true;
  {
    // other state is false 
    Bidding := false;

    // set a deal 
    Deal    := true;
  }

  // The party is ended
  method FinishPost()
  modifies this;
  requires Valid();ensures Valid();
  requires Deal     == true;
  ensures  Finished == true;
  {
    // other state is false 
    Deal     := false;

    // set a deal 
    Finished := true;
  }

  // every state expect finshed state 
  // can check out the cancel state 
  method Cancel()
  modifies this;
  requires Valid();ensures Valid();
  requires Finished == false;
  ensures Canceled == true;
  {
    // other state is false 
    Bidding := false;
    Deal    := false;
    
    // set the canceled is true
    Canceled := true;
  }
}
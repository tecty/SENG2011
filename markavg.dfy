

class Mark{
    var markval : int;
    var bidder : bid;

    predicate Validmark(s : int)
        reads this
    {
        assert (s >= 0 && s<=5);
    }

    constructor(input : int)
        ensures  Validmark(input)
    {
        markval := s;
    }

    method addmark(marklist: seq<int>)
        ensures marklist.Length > 0
    {
        marklist := marklist + [markval];
        assert forall i :: 0 <= i <= |marklist| ==> marklist == marklist[..i] + marklist[i..];
    }
}

method avgmark(list : seq<int>) returns (avg : int)
     requires |list| > 0
{
    var i :int := 0;
    var sum : int := 0;
    avg := 0;
    while i < |list|
    invariant i <= |list|
    {
        sum := sum + list[i];
        i := i+1;
    }
    avg := sum / |list|;
}
//Proving merge sort
//ISSUE: it be verified on local IDE, 
//       but it times out while verifying on the website dafny
predicate permutation(a: seq<int>, b: seq<int>)
{
  a == b || multiset(a) == multiset(b)
}

// To make Dafny know the elements in 2 subseq of a sequence is the same as the elements in this whole sequnce 
lemma  MutisetAddingLemma(a: array<int>,l:int, m: int, u:int)
  requires 0<=l<=m<=u<a.Length
  ensures multiset(a[l..m]) + multiset(a[m..u+1]) == multiset(a[l..u+1])
{
    assert a[l..m] + a[m..u+1] == a[l..u+1];
}

predicate sortedBetween(a :array<int>, start : int, end : int)
  reads a;
  requires 0<= start < a.Length
  requires 0<= end < a.Length
{
  forall i,j:: start <= i < j <= end ==> a[i] <= a[j]
}

predicate Sorted(a :array<int>)
  reads a;
{
  forall q,r:: 0 <= q < r < a.Length ==> a[q] <= a[r]
}

method MergeSort(a1:array<int>) returns (a:array<int>)
  requires a1.Length > 0;
  ensures Sorted(a);
  ensures permutation(a[..], old(a)[..]);
{
  a := mergesort(a1, 0, a1.Length-1);
}

method mergesort(a1:array<int>, l:int, u:int) returns (a:array<int>)
  requires a1.Length > 0;
  requires 0 <= l <= u < a1.Length;
  ensures a.Length == a1.Length;
  ensures sortedBetween(a,l,u);
  ensures forall q:: (0 <= q < l || u < q < a.Length) ==> a[q] == a1[q];
  ensures permutation(a[l..u+1], a1[l..u+1]);
  // ensures multiset(a[l..u+1]) == multiset(a1[l..u+1]);
  ensures a[0..l] == a1[0..l];
  ensures a[u+1..] == a1[u+1..];
  decreases u-l;
{
  a := new int[a1.Length];
  copyArray(a1, a);
  if (l <  u){
    var m:int := (l + u) / 2;
    a := mergesort(a1, l, m);
    assert a[m+1..u+1] == a1[m+1..u+1];
    a := mergesort(a, m+1, u);

    assert permutation(a[l..m+1], a1[l..m+1]);
    assert permutation(a[m+1..u+1],a1[m+1..u+1]);
    MutisetAddingLemma(a,l,m+1,u);
    MutisetAddingLemma(a1,l,m+1,u);
    assert multiset(a[l..u+1]) == multiset(a1[l..u+1]);

    a := merge(a, l, m, u);
  }
}
//this method copy array from a into b
method copyArray(a: array<int>, b: array<int>)
  modifies b;
  requires a.Length  == b.Length
  ensures a.Length == b.Length
  ensures a[..] == b[..]
  // ensures forall k:: 0 <= k < a.Length ==> a[k] == b[k];
{
  var index:= 0;
  while (index < a.Length)
    decreases a.Length - index
    invariant 0 <= index <= a.Length
    invariant a[..] == old(a)[..]
    invariant b[..index] == a[..index]
    invariant b.Length == a.Length
  {
    b[index] := a[index];
    index := index + 1;
  }
}

method merge(a:array<int>, l:int, m:int, u:int) returns (buf:array<int>)
  requires a.Length > 0;
  requires 0 <= l <= m < u < a.Length;
  requires sortedBetween(a,l,m);
  requires sortedBetween(a,m+1,u);
  ensures a.Length == buf.Length;
  ensures multiset(buf[l..u+1]) == multiset(a[l..u+1]);
  ensures sortedBetween(buf,l,u);
  ensures forall i:: (0 <= i < l || u < i < buf.Length) ==> buf[i] == a[i];
{
  buf := new int[a.Length];
  copyArray(a, buf);


  var i:int := l;
  var j:int := m + 1;
  var k:int := 0;
  while (k < u-l+1)
    decreases u-l+1 -k;
    invariant  forall k:: 0 <= k < a.Length ==> a[k] == a[k];
      
    // k is in this buffer index
    invariant 0 <= k <= u-l+1; 
    // j is in the right place
    invariant m+1 <= j <= u+1; 
    // i is in the right place
    invariant l <= i <= m+1; 
    
    // k aligns properly.
    invariant (i-l) + (j-(m+1)) == k; 
    invariant buf.Length == a.Length;
    // elements maintain the same
    invariant multiset(buf[l..l+k]) == multiset(a[l..i]) + multiset(a[m+1..j]);  
    invariant buf[0..l] == a[0..l];
    invariant buf[u+1..] == a[u+1..];
    // buf is sorted in [l,k+l].
    invariant forall q,r:: l <= q < r <= k+l-1 ==>  buf[q] <= buf[r]; 
    invariant forall q,r:: l <= q < l+k && (i <= r <= m || j <= r <= u) ==> buf[q] <= a[r];
  {
    if (i > m)
    {
      buf[l+k] := a[j];
      j := j + 1;
    }
    else if (j > u)
    {
      buf[l+k] := a[i];
      i := i + 1;
    }
    else if (a[i] <= a[j])
    {
      buf[l+k] := a[i];
      i := i + 1;
    }
    else
    {
      buf[l+k] := a[j];
      j := j + 1;
    }
    k := k + 1;
  }
  MutisetAddingLemma(buf,l,m+1,u);
  MutisetAddingLemma(a,l,m+1,u);
  assert  buf[..l] + buf[l..u+1] + buf[u+1..] == buf[..];
  assert  a[..l] + a[l..u+1] + a[u+1..] == a[..];
  assert multiset(buf[0..l]) + multiset(buf[l..u+1]) + multiset(buf[u+1..]) == multiset(buf[..]);
  assert multiset(a[0..l]) + multiset(a[l..u+1]) + multiset(a[u+1..]) == multiset(a[..]);
  assert multiset(buf[u+1..]) == multiset(a[u+1..]);
  assert multiset(buf[0..l]) == multiset(a[0..l]);
  assert multiset(buf[l..u+1]) == multiset(a[l..u+1]);
  assert multiset(buf[..]) == multiset(a[..]);
}

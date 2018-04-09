Param ( 
    [Parameter(Mandatory = $true)]
    [String]$ArtistName 
)

python lyric_bot.py $ArtistName
python train.py --data_dir=./data/$ArtistName
python train.py --data_dir=./data/$ArtistName
python sample.py -n 240
python twitter_access.py $ArtistName

if ($Host.Name -eq "ConsoleHost")
{
    Write-Host "Press any key to continue..."
    $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyUp") > $null
}